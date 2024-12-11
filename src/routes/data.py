from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src import schemas
from src.data import sql_dao_data, sql_dao_users, models
from src.data.database import engine
from src.dependencies import get_db

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/{sector}/", response_model=schemas.Data)
def read_item(
        sector: str,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    if not sql_dao_users.check_token(db, token):
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    item = sql_dao_data.get_item(sector, db)
    return item


@router.get("/all/{sector}/", response_model=list[schemas.Data])
def read_all_items(
        sector: str,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    if not sql_dao_users.check_token(db, token):
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    items = sql_dao_data.get_all_items(sector, db)
    return items


@router.post("/", response_model=schemas.Data)
def create_item(
        data: schemas.DataCreate,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    if not sql_dao_users.check_token(db, token):
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return sql_dao_data.create_item(db, data)
