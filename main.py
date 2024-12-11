from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.data.database import engine, Base
from src.routes import data, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(data.router)
app.include_router(auth.router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (puedes restringir esto más adelante)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los headers
)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
