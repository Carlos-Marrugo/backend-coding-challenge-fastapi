from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from model import Job
from schemas import JobCreate, JobResponse
from services import create_job
from workers import process_job

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/jobs", response_model=JobResponse)
def create_job_endpoint(
    payload: JobCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    job = create_job(db, payload.text)
    background_tasks.add_task(process_job, db, job)

    return JobResponse(
        job_id=job.id,
        status=job.status,
        result=None,
    )


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job_endpoint(job_id: str, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobResponse(
        job_id=job.id,
        status=job.status,
        result=job.result,
    )
