from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Potestades.com")

app.mount(
    "/", StaticFiles(directory="potestades/public", html=True), name="static_page"
)
