from sqlalchemy.orm import Session
from sqlalchemy import desc
from src.data import models
from src import schemas
from datetime import datetime, date

def get_item(sector: str, db: Session):
    today = date.today()
    return db.query(models.Data) \
        .filter(models.Data.date == today) \
        .filter(models.Data.sector == sector) \
        .order_by(desc(models.Data.hour))\
        .first()

def get_all_items(sector:str, db: Session):
    today = date.today()
    return db.query(models.Data) \
        .filter(models.Data.date == today) \
        .filter(models.Data.sector == sector) \
        .order_by(desc(models.Data.hour)) \
        .all()

def create_item(db: Session, data: schemas.DataCreate):
    db_item = models.Data(
        sector=data.sector,
        temperature=data.temperature,
        date=datetime.strptime(data.date, '%Y-%m-%d').date(),
        hour=datetime.strptime(data.hour, '%H:%M:%S').time()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item: models.Data):
    db.delete(item)
    db.commit()
