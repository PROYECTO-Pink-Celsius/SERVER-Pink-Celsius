from fastapi import FastAPI
from src.routes import data
from src.data.database import engine

app = FastAPI()


# Crear las tablas en la base de datos
def create_tables():
    from src.data.models import Base
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    create_tables()

# Registrar las rutas
app.include_router(data.router)


# uvicorn src.main:app --reload
# uvicorn src.main:app --host 192.168.1.200 --port 8000
