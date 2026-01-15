from fastapi import FastAPI

from database import init_db

app = FastAPI(
    title="Backend Coding Challenge",
    description="Asynchronous job processing API built with FastAPI",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}