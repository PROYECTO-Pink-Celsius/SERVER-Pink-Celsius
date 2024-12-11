from datetime import datetime, date, timedelta

from sqlalchemy import desc
from sqlalchemy.orm import Session

from src import schemas
from src.data.models import Data


def get_item(sector: str, db: Session):
    # Obtener la fecha de hoy sin la parte de la hora (combinando con la medianoche)
    today = datetime.combine(date.today(), datetime.min.time())

    # Obtener el último ítem con fecha de hoy y el sector específico
    data = (
        db.query(Data)
        .filter(Data.date >= today)
        .filter(Data.sector == sector)
        .order_by(desc(Data.date))
        .first()
    )

    if not data:
        data = {
            "sector": sector,
            "temperature": "NO DATA",
            "id": -1,
            "date": datetime.now()
        }
    return data


def get_all_items(sector: str, db: Session):
    # Obtener la fecha y hora de hace 12 horas
    twelve_hours_ago = datetime.now() - timedelta(hours=12)

    # Obtener todos los ítems de las últimas 12 horas y el sector específico
    all_data = (
        db.query(Data)
        .filter(Data.date >= twelve_hours_ago)  # Filtrar por fecha de las últimas 12 horas
        .filter(Data.sector == sector)
        .order_by(desc(Data.date))  # Ordenar por fecha descendente
        .all()
    )

    # Si no se encuentran datos, agregar un ítem con "NO DATA"
    if not all_data:
        all_data.append({
            "sector": sector,
            "temperature": "NO DATA",
            "id": -1,
            "date": datetime.now()
        })

    return all_data

def create_item(db: Session, data: schemas.DataCreate):
    db_item = Data(
        sector=data.sector,
        temperature=data.temperature,
        date=datetime.now()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item: Data):
    db.delete(item)
    db.commit()
