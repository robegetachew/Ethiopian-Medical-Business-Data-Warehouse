from sqlalchemy import Column, BigInteger, String, Double
from .database import Base


class MedicalTelegramMessage(Base):
    __tablename__ = "Medical_DataWarehouse"
    id = Column(BigInteger, primary_key=True, index=True)
    channel_username = Column(String, nullable=True)
    channel_title = Column(String, nullable=True)
    message = Column(String, nullable=True)
    message_id = Column(String, nullable=True)


class Detection(Base):
    __tablename__ = 'detections'
    id = Column(BigInteger, primary_key=True, nullable=False)  
    filename = Column(String, nullable=True)
    x_min = Column(Double, nullable=True)
    y_min = Column(Double, nullable=True)
    x_max = Column(Double, nullable=True)
    y_max = Column(Double, nullable=True)