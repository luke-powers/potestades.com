import logging

from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from shurl_log import process_logging

from shurlrtener import lengthener, setter, shortener, show

process_logging(logging)

APP = FastAPI(title="potestades.com", docs_url=None, redoc_url=None, openapi_url=None)
APP.add_middleware(HTTPSRedirectMiddleware)


@APP.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("personal/static/img/favicon.ico")


@APP.get("/shorten/{url:path}")
async def sh(request: Request, url: str):
    return await shortener(request, url)


@APP.get("/set/{code}/{url:path}")
async def se(request: Request, code: str, url: str):
    return await setter(request, code, url)


@APP.get("/{code}")
async def len(code: str):
    return await lengthener(code)


@APP.get("/show/")
async def sho():
    return await show()


APP.mount("/coach", StaticFiles(directory="coach/public", html=True), name="Coach Page")

APP.mount(
    "/", StaticFiles(directory="personal/public", html=True), name="Personal Page"
)
