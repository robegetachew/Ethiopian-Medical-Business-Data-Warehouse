from pydantic import BaseModel, ConfigDict

# MedicalTelegramMessage Schemas
class MedicalTelegramMessageBase(BaseModel):
    channel_username: str | None = None
    channel_title: str | None = None
    message: str | None = None

    model_config = ConfigDict(from_attributes=True)


class MedicalTelegramMessageCreate(MedicalTelegramMessageBase):
    pass


class MedicalTelegramMessage(MedicalTelegramMessageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# Detection Schemas
class DetectionBase(BaseModel):
    filename: str | None = None
    x_min: float | None = None
    y_min: float | None = None
    x_max: float | None = None
    y_max: float | None = None

    model_config = ConfigDict(from_attributes=True)


class DetectionCreate(DetectionBase):
    pass


class Detection(DetectionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)