"""
WSGI config for OmniDB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.asgi import get_asgi_application

from . import startup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OmniDB.settings")

application = get_asgi_application()

# Startup Procedure
# startup.startup_procedure()
