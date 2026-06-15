from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="src/html")
app.mount("/assets", StaticFiles(directory="src/assets"), name="assets")
