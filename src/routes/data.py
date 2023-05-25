from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.data.database import engine
from ..data import crud, models
from .. import schemas
from ..dependencies import get_db

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/api/data",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)
# @router.get("/{item_id}", response_model=schemas.Data)
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     item = crud.get_item(db, item_id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item


@router.get("/all/{sector}", response_model=None)
def read_all_items(sector: str, db: Session = Depends(get_db)):
    items = crud.get_all_items(sector, db)
    return items

@router.get("/{sector}", response_model=None)
def read_item(sector: str, db: Session = Depends(get_db)):
    item = crud.get_item(sector, db)
    return item

@router.post("/", response_model=schemas.Data)
def create_item(data: schemas.DataCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, data)

# @router.delete("/{item_id}")
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     item = crud.get_item(db, item_id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     crud.delete_item(db, item)
#     return {"message": "Item deleted"}
