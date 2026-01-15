from sqlalchemy.orm import Session

from model import Job
from constants import JobStatus


def create_job(db: Session, text: str) -> Job:
    job = Job(text=text, status=JobStatus.PENDING)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def update_job_status(db: Session, job: Job, status: JobStatus):
    job.status = status
    db.commit()
    db.refresh(job)


def save_job_result(db: Session, job: Job, result: dict):
    job.result = result
    job.status = JobStatus.COMPLETED
    db.commit()
    db.refresh(job)
