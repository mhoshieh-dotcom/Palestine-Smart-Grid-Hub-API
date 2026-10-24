from sqlalchemy import Column, Integer, String
from database import Base 

class Station(Base):
    __tablename__ = "stations_orm" 

    id = Column(Integer, primary_key=True, index=True) # SERIAL PRIMARY KEY
    city = Column(String(50), nullable=False)           # VARCHAR(50) NOT NULL
    capacity_mw = Column(Integer, nullable=False)       # INT NOT NULL
    status = Column(String(20), nullable=False)         # VARCHAR(20) NOT NULL

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False) 