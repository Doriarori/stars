from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker, declarative_base

URL = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/query'

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class StarDB(Base):
    __tablename__ = 'star_skigin'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    temperature = Column(Integer, nullable=False)  # Temperature in Kelvin
    size = Column(Float, nullable=False)  # Size in solar radii
    distance = Column(Float, nullable=False)  # Distance from Earth in light years
