import os
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

from database import database as database
from database.database import StarDB
from model.model import Star

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {'message': 'Service alive'}


@app.post("/add_star")
async def add_star(star: Star, db: db_dependency):
    new_star = StarDB(**star.dict())
    db.add(new_star)
    db.commit()
    db.refresh(new_star)
    return new_star


@app.get("/stars")
async def list_stars(db: db_dependency):
    stars = db.query(StarDB).all()
    return stars


@app.get("/get_star_by_id/{star_id}")
async def get_star_by_id(star_id: int, db: db_dependency):
    star = db.query(StarDB).filter(StarDB.id == star_id).first()
    if not star:
        raise HTTPException(status_code=404, detail="Star not found")
    return star


@app.delete("/delete_star/{star_id}")
async def delete_star(star_id: int, db: db_dependency):
    star = db.query(StarDB).filter(StarDB.id == star_id).first()
    if not star:
        raise HTTPException(status_code=404, detail="Star not found")
    db.delete(star)
    db.commit()
    return {"message": "Star deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
