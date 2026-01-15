from typing import Optional, List
from pydantic import BaseModel

from constants import JobStatus


class JobCreate(BaseModel):
    text: str


class TopWord(BaseModel):
    word: str
    count: int


class JobResult(BaseModel):
    word_count: int
    character_count: int
    top_words: List[TopWord]


class JobResponse(BaseModel):
    job_id: str
    status: JobStatus
    result: Optional[JobResult] = None
