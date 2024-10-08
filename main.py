from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="potestades.com")
app.add_middleware(HTTPSRedirectMiddleware)

app.mount(
    "/", StaticFiles(directory="personal/public", html=True), name="Personal Page"
)
