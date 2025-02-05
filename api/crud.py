from sqlalchemy.orm import Session
from api import models, schemas

# MedicalTelegramMessage CRUD
def get_medical_telegram_message(db: Session, message_id: int):
    return db.query(models.MedicalTelegramMessage).filter(models.MedicalTelegramMessage.id == message_id).first()


def get_medical_telegram_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MedicalTelegramMessage).offset(skip).limit(limit).all()


def create_medical_telegram_message(db: Session, message: schemas.MedicalTelegramMessageCreate):
    db_message = models.MedicalTelegramMessage(**message.model_dump())  # changed to model_dump
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Detection CRUD
def get_detection(db: Session, detection_id: int):
    return db.query(models.Detection).filter(models.Detection.id == detection_id).first()


def get_detections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detection).offset(skip).limit(limit).all()


def create_detection(db: Session, detection: schemas.DetectionCreate):
    db_detection = models.Detection(**detection.model_dump()) # changed to model_dump
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection