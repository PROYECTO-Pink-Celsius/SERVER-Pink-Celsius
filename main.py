from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from src.routes import data
from src.data.database import engine

app = FastAPI()
app.include_router(data.router)


# Crear las tablas en la base de datos
def create_tables():
    from src.data.models import Base
    Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.on_event("startup")
def startup_event():
    create_tables()

# Registrar las rutas


# uvicorn main:app --reload
# uvicorn main:app --host 192.168.1.127 --port 8000
