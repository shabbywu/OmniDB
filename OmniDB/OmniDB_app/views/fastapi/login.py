import logging

from django.conf import settings
from django.contrib.auth import authenticate, login
from jose import jwt
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, HTTPException
from OmniDB import settings
from OmniDB_app.include.Session import Session
from OmniDB_app.models import Connection, Technology
from OmniDB_app.views.fastapi import app, dependencies, schemas
from django.contrib.auth import get_user_model
from OmniDB_app.include import OmniDatabase
from fastapi.security import OAuth2PasswordRequestForm
from contextlib import contextmanager


UserModel = get_user_model()
logger = logging.getLogger(__name__)


@app.get("/")
def check_session(
    django_session=Depends(dependencies.get_django_session),
    v_session=Depends(dependencies.get_or_create_omnidb_session),
):
    return RedirectResponse(
        settings.PATH
        + f"/workspace?{settings.SESSION_COOKIE_NAME}={django_session.session_key}"
    )


@app.post("/check_session_message/")
def check_session_message(
    user=Depends(dependencies.get_user),
    django_session=Depends(dependencies.get_django_session),
    v_return=Depends(dependencies.get_default_return),
):
    if django_session.get("omnidb_alert_message"):
        v_return["v_data"] = django_session.get("omnidb_alert_message")
        django_session["omnidb_alert_message"] = ""

    return v_return


@app.post("/sign_in_api/", tags=["LOGIN"])
def sign_in_api(
    request=Depends(dependencies.get_django_request),
    json_object=Depends(dependencies.parse_json_object),
    django_session=Depends(dependencies.get_django_session),
    v_return=Depends(dependencies.get_default_return),
):
    username = json_object["p_username"]
    pwd = json_object["p_pwd"]

    user = authenticate(username=username, password=pwd)
    if user is not None:
        login(request, user)
    else:
        return v_return

    django_session.save()
    logger.info('User "{0}" logged in.'.format(username))
    v_return["v_data"] = django_session.session_key
    return v_return


@app.post("/sign_in_with_database/", tags=["LOGIN"])
def sign_in_with_database(
    payload: schemas.LoginWithDatabasePayload,
    request=Depends(dependencies.get_django_request),
    django_session=Depends(dependencies.get_django_session),
    v_return=Depends(dependencies.get_default_return),
    sys_user=Depends(dependencies.get_sys_api_caller),
):
    try:
        user = UserModel.objects.get(username=payload.username)
    except UserModel.DoesNotExist:
        user = UserModel.objects.create_user(
            username=payload.username,
            password=payload.username,
            email=f"{payload.username}@zhiyi.com",
            is_staff=True,
        )

    login(request, user)

    with contextmanager(dependencies.get_or_create_omnidb_session)(
        django_session=django_session, user_details=dependencies.get_user_detail(user)
    ) as v_session:
        conn, _ = Connection.objects.update_or_create(
            user=user,
            technology=Technology.objects.get(name=payload.type),
            server=payload.credential.host,
            port=payload.credential.port,
            database=payload.credential.db_name,
            username=payload.credential.username,
            defaults=dict(
                password=payload.credential.password,
                alias=str(payload.credential),
                public=False,
            ),
        )
        conn.save()

        database = OmniDatabase.Generic.InstantiateDatabase(
            conn.technology.name,
            conn.server,
            conn.port,
            conn.database,
            conn.username,
            conn.password,
            conn.id,
            conn.alias,
            p_conn_string=conn.conn_string,
            p_parse_conn_string=True,
        )
        v_session.AddDatabase(
            p_conn_id=conn.id,
            p_technology=Technology.objects.get(name=payload.type).name,
            p_database=database,
            p_prompt_password=True,
            p_tunnel_information=None,
            p_alias=conn.alias,
            p_public=False,
        )

    v_return["v_data"] = v_session.v_user_key
    return v_return


@app.post("/token", response_model=schemas.Token, tags=["LOGIN"])
async def grant_jwt_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """调试用"""
    sys_user = {"platform": form_data.username}
    if not sys_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = jwt.encode(sys_user, settings.JWT["SECRET_KEY"], algorithm=settings.JWT["ALGORITHMS"][0])
    return {"access_token": access_token, "token_type": "bearer"}


