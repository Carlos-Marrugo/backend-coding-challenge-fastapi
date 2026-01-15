from collections import Counter
from sqlalchemy.orm import Session

from model import Job
from constants import JobStatus
from services import update_job_status, save_job_result


def process_job(job_id: int):
    from database import SessionLocal

    db: Session = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            print(f"Job {job_id} not found")
            return

        update_job_status(db, job, JobStatus.PROCESSING)

        text = None

        if hasattr(job, 'text') and job.text:
            text = job.text
        elif job.payload and 'text' in job.payload:
            text = job.payload['text']
        else:
            text = job.name

        if not text:
            update_job_status(db, job, JobStatus.FAILED)
            return

        words = text.split()

        word_count = len(words)
        character_count = len(text)

        word_frequencies = Counter(words)
        top_words = [
            {"word": word, "count": count}
            for word, count in word_frequencies.most_common(5)
        ]

        result = {
            "word_count": word_count,
            "character_count": character_count,
            "top_words": top_words,
        }

        save_job_result(db, job, result)

        print(f"Job {job_id} processed successfully")

    except Exception as e:
        print(f"Error processing job {job_id}: {e}")
        if 'job' in locals() and job:
            update_job_status(db, job, JobStatus.FAILED)
    finally:
        db.close()