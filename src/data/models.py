from sqlalchemy import Column, Integer, String, Date, DateTime

from src.data.database import Base


class User(Base):
    __tablename__ = 'users'

    name = Column(String(255), primary_key=True)
    password_hash = Column(String(255))
    token = Column(String(255), unique=True)
    expires_at = Column(Date)


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String)
    temperature = Column(String)
    date = Column(DateTime)
