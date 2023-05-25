from sqlalchemy import Column, Integer, String, Date, Time
from src.data.database import Base

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String)
    temperature = Column(String)
    date = Column(Date)
    hour = Column(Time)
