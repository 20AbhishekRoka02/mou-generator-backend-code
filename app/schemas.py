
from uuid import UUID, uuid4

from click import DateTime
from pydantic import BaseModel, Field
from datetime import datetime

class CollegeBase(BaseModel):
    college_id: UUID = Field(default_factory=uuid4)
    college_name: str
    address: str
    official_email: str
    official_phone: str
    signatory: str
    logo_id: UUID = Field(default_factory=uuid4)
    verified: bool
    class Config:
        orm_mode = True
        
class MediaBase(BaseModel):
    media_id : UUID = Field(default_factory=uuid4)
    filename: str
    size: float
    upload_date: datetime

class GetProjectData(BaseModel):
    project_id : int
    project_name : str
    purpose : str
    context : str
    pass

# class getMoUData(BaseModel):
#     project_ids: list
#     start_date: datetime
#     duration: int