## WorkFlow
<img width="1330" height="809" alt="image" src="https://github.com/user-attachments/assets/e5fcea78-b332-42a0-93ef-6b2822bdfe67" />

# Backend Coding Challenge – Asynchronous Job Processing API

## Overview

This project is an asynchronous job processing API built with **FastAPI**. It provides a simple interface for submitting jobs, processing them in the background, and retrieving their execution status.

---

## What This API Does

The API exposes endpoints that allow clients to:

* Submit a job with a name and arbitrary payload
* Process jobs asynchronously in the background
* Retrieve the current status and details of a job

Each job is persisted in a database and transitions through its lifecycle independently of the request that created it.

---

## Architecture

The application follows a modular structure:

* **Routers** handle HTTP request/response logic
* **Schemas** define request and response models
* **Models** define database entities
* **Services** contain business logic
* **Workers** process jobs asynchronously
* **Database layer** manages persistence and sessions

This structure keeps concerns separated and the codebase easy to maintain.

---

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Create Job

```
POST /jobs
```

Request body:

```json
{
  "name": "data-processing-test",
  "payload": {
    "source": "csv",
    "rows": 1000
  }
}
```

Response (201 Created):

```json
{
  "id": 1,
  "name": "data-processing-test",
  "status": "pending",
  "payload": {
    "source": "csv",
    "rows": 1000
  },
  "created_at": "2026-01-15T01:12:00"
}
```

---

### Get Job

```
GET /jobs/{job_id}
```

Response (200 OK):

```json
{
  "id": 1,
  "name": "data-processing-test",
  "status": "completed",
  "payload": {
    "source": "csv",
    "rows": 1000
  },
  "created_at": "2026-01-15T01:12:00"
}
```

If the job does not exist:

Response (404 Not Found):

```json
{
  "detail": "Job not found"
}
```

---

## Background Processing

Jobs are processed asynchronously using FastAPI background tasks. This allows job execution to occur outside the request lifecycle while keeping the API responsive.

---

## Database

The application stores job data in a `jobs` table with the following fields:

* `id`
* `name`
* `payload`
* `status`
* `created_at`

SQLite is used for local development.

---

## Running the Application

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
uvicorn main:app --reload
```

### Access

* API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
* Health endpoint: [http://localhost:8000/health](http://localhost:8000/health)

---

## Notes

* The current implementation uses FastAPI `BackgroundTasks` for simplicity
* The design can be extended to external workers or message queues
* The project focuses on clarity, correctness, and maintainable structure


## Summary

This project demonstrates a clean and practical approach to building an asynchronous backend API using FastAPI. It focuses on real-world backend patterns, clear design decisions, and maintainable code structure, making it a solid foundation for scalable job-based systems.
