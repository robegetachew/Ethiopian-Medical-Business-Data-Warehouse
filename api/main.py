from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api import crud, models, schemas
from api.database import SessionLocal, engine

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MedicalTelegramMessage Endpoints
@app.post("/messages/", response_model=schemas.MedicalTelegramMessage)
async def create_message(
    message: schemas.MedicalTelegramMessageCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_medical_telegram_message(db=db, message=message)


@app.get("/messages/{message_id}", response_model=schemas.MedicalTelegramMessage)
async def read_message(
    message_id: int, 
    db: Session = Depends(get_db)
):
    db_message = crud.get_medical_telegram_message(db=db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message


@app.get("/messages/", response_model=list[schemas.MedicalTelegramMessage])
async def read_messages(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    messages = crud.get_medical_telegram_messages(db=db, skip=skip, limit=limit)
    return messages

# Detection Endpoints
@app.post("/detections/", response_model=schemas.Detection)
async def create_detection(
    detection: schemas.DetectionCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_detection(db=db, detection=detection)


@app.get("/detections/{detection_id}", response_model=schemas.Detection)
async def read_detection(
    detection_id: int, 
    db: Session = Depends(get_db)
):
    db_detection = crud.get_detection(db=db, detection_id=detection_id)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection


@app.get("/detections/", response_model=list[schemas.Detection])
async def read_detections(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    detections = crud.get_detections(db=db, skip=skip, limit=limit)
    return detections