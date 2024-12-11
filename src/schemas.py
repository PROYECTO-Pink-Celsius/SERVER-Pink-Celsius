from datetime import datetime

from pydantic import BaseModel


class DataCreate(BaseModel):
    sector: str
    temperature: str

class Data(DataCreate):
    id: int
    date: datetime

    class Config:
        from_attributes = True


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
