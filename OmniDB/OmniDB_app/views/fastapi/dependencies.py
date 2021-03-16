import logging
import json
from typing import Dict, TypeVar

from fastapi import Depends, Form, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from OmniDB_app.models.main import UserDetails
from OmniDB_app.include.Session import Session
from OmniDB_app.views.memory_objects import get_database_object
from jose import jwt, JWTError
from django.conf import settings


logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
M = TypeVar("M")


def parse_json_object(data=Form(None)) -> Dict:
    if data:
        return json.loads(data)
    raise HTTPException(
        405,
        detail=dict(
            v_data="",
            v_error=True,
            v_error_id=1,
        ),
    )


def get_django_request(request: Request):
    try:
        return request.scope["__django_request__"]
    except KeyError:
        raise


def get_django_session(request: Request) -> Dict:
    try:
        return request.scope["__django_session__"]
    except KeyError:
        raise


def get_user(request: Request):
    try:
        user = request.scope["__django_user__"]
        logger.info(
            "user<%s>.is_authenticated=%s", user.username, user.is_authenticated
        )
        assert user.is_authenticated
        return user
    except Exception:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail=dict(
                v_data="",
                v_error=True,
                v_error_id=1,
            ),
        )


def get_user_detail(user=Depends(get_user)):
    # User is authenticated, check if user details object exists.
    try:
        user_details = UserDetails.objects.get(user=user)
    # User details does not exist, create it.
    except Exception:
        user_details = UserDetails(user=user)
        user_details.save()
    return user_details


def get_omnidb_session(django_session=Depends(get_django_session)):
    omnidb_session = django_session.get("omnidb_session")
    if omnidb_session is None:
        # Invalid session
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail=dict(
                v_data="",
                v_error=True,
                v_error_id=1,
            ),
        )
    yield omnidb_session
    django_session["omnidb_session"] = omnidb_session


def get_or_create_omnidb_session(
    django_session=Depends(get_django_session), user_details=Depends(get_user_detail)
):
    omnidb_session = django_session.get("omnidb_session")
    if not omnidb_session:
        # creating session key to use it
        django_session.save()

        omnidb_session = Session(
            user_details.user.id,
            user_details.user.username,
            "light",
            user_details.font_size,
            user_details.user.is_superuser,
            django_session.session_key,
            user_details.csv_encoding,
            user_details.csv_delimiter,
        )

        django_session["omnidb_session"] = omnidb_session
    yield omnidb_session
    django_session["omnidb_session"] = omnidb_session


def require_database(p_check_timeout=True, p_open_connection=True):
    def get_database(
        django_session=Depends(get_django_session),
        v_session=Depends(get_omnidb_session),
        json_object=Depends(parse_json_object),
    ):
        v_return = dict(
            v_data="",
            v_error=True,
            v_error_id=1,
        )
        v_database_index = json_object["p_database_index"]
        v_tab_id = json_object["p_tab_id"]

        if v_database_index is not None:
            try:
                if p_check_timeout:
                    # Check database prompt timeout
                    v_timeout = v_session.DatabaseReachPasswordTimeout(
                        int(v_database_index)
                    )
                    if v_timeout["timeout"]:
                        v_return["v_data"] = {
                            "password_timeout": True,
                            "message": v_timeout["message"],
                        }
                        v_return["v_error"] = True
                        raise HTTPException(400, detail=v_return)

                v_database = get_database_object(
                    p_session=django_session,
                    p_tab_id=v_tab_id,
                    p_database_index=v_database_index,
                    p_attempt_to_open_connection=p_open_connection,
                )
            except Exception as exc:
                v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
                v_return["v_error"] = True
                raise HTTPException(400, detail=v_return)
        else:
            v_database = None

        return v_database

    return Depends(get_database)


def get_sys_api_caller(token=Depends(oauth2_scheme)) -> Dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT["SECRET_KEY"], algorithms=settings.JWT["ALGORITHMS"])
        platform: str = payload.get("platform")
        if platform is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return payload



def get_cryptor(django_session=Depends(get_django_session)):
    cryptor = django_session.get("cryptor")
    yield cryptor


def get_default_return():
    return dict(
        v_data="",
        v_error=False,
        v_error_id=-1,
    )
