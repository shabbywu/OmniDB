from django.conf import settings
from django.contrib.sessions.middleware import (
    SessionMiddleware,
    SuspiciousOperation,
    UpdateError,
)


class QueryTokenSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        session_key = request.GET.get(settings.SESSION_COOKIE_NAME)
        request.session = self.SessionStore(session_key)

    def process_response(self, request, response):
        try:
            accessed = request.session.accessed
            modified = request.session.modified
            empty = request.session.is_empty()
        except AttributeError:
            return response
        if modified and not empty:
            if response.status_code != 500:
                try:
                    request.session.save()
                except UpdateError:
                    raise SuspiciousOperation(
                        "The request's session was deleted before the "
                        "request completed. The user may have logged "
                        "out in a concurrent request, for example."
                    )
        return response
