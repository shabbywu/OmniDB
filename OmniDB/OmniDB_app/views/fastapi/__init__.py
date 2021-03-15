from django.core.handlers.asgi import ASGIRequest
from django.http import HttpResponse
from fastapi import Depends, FastAPI
from OmniDB_app.views.fastapi.dependencies import get_omnidb_session
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import Message


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    headers = getattr(exc, "headers", None)
    if headers:
        return JSONResponse(exc.detail, status_code=exc.status_code, headers=headers)
    else:
        return JSONResponse(exc.detail, status_code=exc.status_code)


app = FastAPI(exception_handlers={HTTPException: http_exception_handler})


class FastAPIContext:
    def __init__(self, request: ASGIRequest):
        self.request = request
        request.scope["__django_request__"] = request
        request.scope["__django_session__"] = request.session
        request.scope["__django_user__"] = request.user
        self.raw_response = dict(status=200, content=b"")
        self.headers = {}

    async def receive(self) -> Message:
        return {"type": "http.request", "body": self.request.body}

    async def send(self, message: Message):
        if message["type"] == "http.response.start":
            self.raw_response["status"] = message["status"]
        elif message["type"] == "http.response.body":
            self.raw_response["content"] = message["body"]
        if "headers" in message:
            for header in message["headers"]:
                self.headers[header[0]] = header[1]

    async def __call__(self, handler):
        await handler(self.request.scope, self.receive, self.send)
        response = HttpResponse(**self.raw_response)
        for k, v in self.headers.items():
            response[k] = v
        return response


async def dispatch_fastapi_view(request: ASGIRequest, *args, **kwargs):
    context = FastAPIContext(request)
    response = await context(app)
    return response


from . import login, tree_mysql, tree_postgresql, workspace  # noqa
