from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import engine, Base, get_db
import models
import schemas
import auth 
import ai_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Palestine Smart Grid Hub API", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "Online", "project": "Palestine Smart Grid Hub", "version": "1.0.0"}


@app.get("/stations", response_model=List[schemas.StationResponse])
def get_all_stations(db: Session = Depends(get_db)):
    stations = db.query(models.Station).all()
    return stations

@app.post("/add-station", response_model=schemas.StationResponse)
def add_new_station(new_station: schemas.StationCreate, db: Session = Depends(get_db)):
    existing_station = db.query(models.Station).filter(models.Station.city == new_station.name).first()
    if existing_station:
        raise HTTPException(status_code=400, detail="Station already exists in the system")
    
    db_station = models.Station(
        city=new_station.name.capitalize(),
        capacity_mw=new_station.capacity_mw,
        status=new_station.status.capitalize()
    )
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station


@app.post("/signup", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pass = auth.hash_password(user_data.password)
    
    new_user = models.User(
        email=user_data.email,
        hashed_password=hashed_pass
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login", response_model=schemas.Token)
def login(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Email or Password")
    
    if not auth.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Email or Password")
    
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/ai/analyze-db-load")
def analyze_database_grid_load(db: Session = Depends(get_db)):
    stations_in_db = db.query(models.Station).all()
    
    if not stations_in_db:
        raise HTTPException(status_code=404, detail="No active grid data found in the database.")
    
    db_data_summary = "Live Palestine Smart Grid Status:\n"
    for station in stations_in_db:
        db_data_summary += f"- City: {station.city}, Capacity: {station.capacity_mw}MW, Status: {station.status}\n"
    
    print("--- DEBUGGING DATA SENT TO AI ---")
    print(db_data_summary)
    print("---------------------------------")
    
    ai_report = ai_service.analyze_power_grid_load(grid_data=db_data_summary)
    
    return {
        "status": "Success",
        "source": "PostgreSQL Live Database",
        "engineering_analysis_report": ai_report
    }

