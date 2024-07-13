from pydantic import BaseModel
import datetime


class DataBase(BaseModel):
    sector: str
    temperature: str
    date: datetime.date
    hour: datetime.time


class DataCreate(BaseModel):
    sector: str
    temperature: str
    date: str
    hour: str


class DataUpdate(DataBase):
    pass


class Data(DataBase):
    id: int

    class Config:
        orm_mode = True
