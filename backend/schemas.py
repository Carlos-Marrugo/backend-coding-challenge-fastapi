from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime


class JobCreate(BaseModel):
    name: str
    payload: Dict[str, Any]


class JobResponse(BaseModel):
    id: int
    name: str
    status: str
    payload: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True
