from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import AsyncIterator

from database import init_db
from routers import router as jobs_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:

    print("Starting up...")
    init_db()

    yield

    print("Shutting down...")


app = FastAPI(
    title="Backend Coding Challenge",
    description="Asynchronous job processing API built with FastAPI",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(jobs_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}