from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    company: str | None = Field(None, max_length=150)
    position: str | None = Field(None, max_length=100)
    license_key: str = Field(..., max_length=255)

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    license_key: str
    created_at: datetime  # use datetime, not str

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2
        json_encoders = {
            datetime: lambda v: v.isoformat()  # ensures datetime is serialized as a string
        }
