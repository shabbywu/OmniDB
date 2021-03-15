import logging

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from fastapi import Depends
from OmniDB import settings
from OmniDB_app.include.Session import Session
from OmniDB_app.models.main import *
from OmniDB_app.views.fastapi import app, dependencies

logger = logging.getLogger(__name__)


@app.get("/")
def check_session(
    user=Depends(dependencies.get_user),
    django_session=Depends(dependencies.get_django_session),
):
    # User is authenticated, check if user details object exists.
    try:
        user_details = UserDetails.objects.get(user=user)
    # User details does not exist, create it.
    except Exception:
        user_details = UserDetails(user=user)
        user_details.save()

    # Invalid session
    if not django_session.get("omnidb_session"):
        # creating session key to use it
        django_session.save()

        v_session = Session(
            user.id,
            user.username,
            "light",
            user_details.font_size,
            user.is_superuser,
            django_session.session_key,
            user_details.csv_encoding,
            user_details.csv_delimiter,
        )

        django_session["omnidb_session"] = v_session
    return redirect(
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
