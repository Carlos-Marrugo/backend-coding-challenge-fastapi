# test_simple.py
from database import init_db, SessionLocal
from model import Job

print("1. Initializing db...")
init_db()

print("2. connectiong...")
db = SessionLocal()

print("3. creating test...")
job = Job(
    name='test-simple',
    payload={'text': 'hola mundo'},
    status='pending'
)
db.add(job)
db.commit()
db.refresh(job)
print(f"created: ID={job.id}")

job_db = db.query(Job).filter(Job.id == job.id).first()
print(f"saved in bd: {job_db.name}")

db.close()
