from collections import Counter
from sqlalchemy.orm import Session

from model import Job
from constants import JobStatus
from services import update_job_status, save_job_result


def process_job(db: Session, job: Job):
    update_job_status(db, job, JobStatus.PROCESSING)

    text = job.text
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
