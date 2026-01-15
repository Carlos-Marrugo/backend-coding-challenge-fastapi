from sqlalchemy.orm import Session
from sqlalchemy import JSON

from schemas import JobCreate
from model import Job
from constants import JobStatus


def create_job(db: Session, job_data: JobCreate) -> Job:
    job = Job(
        name=job_data.name,
        payload=job_data.payload,
        status=JobStatus.PENDING,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def update_job_status(db: Session, job: Job, status: JobStatus):
    job.status = status
    db.commit()
    db.refresh(job)


def save_job_result(db: Session, job: Job, result: dict):

    if hasattr(job, 'result'):
        job.result = result

    job.status = JobStatus.COMPLETED
    db.commit()
    db.refresh(job)