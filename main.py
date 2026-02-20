import logging

from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from shurlrtener import shurlrtener
from shurlrtener.shurl_log import process_logging

process_logging(logging)

APP = FastAPI(title="potestades.com", docs_url=None, redoc_url=None, openapi_url=None)
APP.add_middleware(HTTPSRedirectMiddleware)


@APP.on_event("startup")
async def on_startup():
    shurlrtener.on_startup()


@APP.on_event("shutdown")
async def on_shutdown():
    shurlrtener.on_shutdown()


@APP.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("personal/static/img/favicon.ico")


@APP.get("/shorten/{url:path}")
async def sh(request: Request, url: str):
    return await shurlrtener.shortener(request, url)


@APP.get("/set/{code}/{url:path}")
async def se(request: Request, code: str, url: str):
    return await shurlrtener.setter(request, code, url)


@APP.get("/{code}")
async def len(code: str):
    return await shurlrtener.lengthener(code)


@APP.get("/show/")
async def sho():
    return await shurlrtener.show()


APP.mount("/coach", StaticFiles(directory="coach/public", html=True), name="Coach Page")

APP.mount(
    "/", StaticFiles(directory="personal/public", html=True), name="Personal Page"
)
