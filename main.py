from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Potestades.com")
app.add_middleware(HTTPSRedirectMiddleware)

app.mount(
    "/", StaticFiles(directory="public", html=True), name="static_page"
)
