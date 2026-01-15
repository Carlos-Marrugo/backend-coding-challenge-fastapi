## WorkFlow
<img width="1330" height="809" alt="image" src="https://github.com/user-attachments/assets/e5fcea78-b332-42a0-93ef-6b2822bdfe67" />

# Backend Coding Challenge – Asynchronous Job Processing API

## Overview

This project is an asynchronous job processing API built with **FastAPI**. It allows clients to submit long-running tasks (jobs), processes them in the background, and provides endpoints to track the status of each job.

The goal of this project is to demonstrate backend engineering fundamentals such as API design, request validation, background processing, persistence, error handling, and clean architecture.

---

## Why This Project Exists

In real-world systems, many operations cannot be processed synchronously within a single HTTP request. Examples include:

* Processing large files
* Data crawling and ingestion
* Document analysis
* Long-running computations
* AI or ML-related tasks

Blocking an HTTP request for these operations leads to timeouts, poor user experience, and scalability issues. This project demonstrates how to handle such scenarios using asynchronous background processing while keeping the API responsive.

---

## What This API Does

The API provides a simple but realistic workflow:

1. **Create a Job** – Clients submit a job with metadata and payload.
2. **Process the Job Asynchronously** – Jobs are processed in the background without blocking requests.
3. **Track Job Status** – Clients can query the current status of a job at any time.

---

## Architecture Overview

The project follows a clean and modular backend architecture:

* **Routers**: Handle HTTP requests and responses
* **Schemas (Pydantic)**: Validate and serialize request/response data
* **Models (SQLAlchemy)**: Define database schema
* **Services**: Contain business logic
* **Workers**: Handle background job processing
* **Database Layer**: Manages persistence and sessions

This separation of concerns improves maintainability, testability, and scalability.

---

## Technology Stack

* **Python**
* **FastAPI** – Web framework
* **SQLAlchemy** – ORM
* **SQLite** – Database (for simplicity and portability)
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server

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

### Create a Job

```
POST /jobs
```

Request Body:

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

### Get Job Status

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

Jobs are processed asynchronously using FastAPI’s `BackgroundTasks`. This ensures:

* HTTP requests return immediately
* Long-running work happens outside the request lifecycle
* The system remains responsive under load

While `BackgroundTasks` is used here for simplicity, the design can be easily extended to real-world systems such as Celery, AWS SQS, or Kafka.

---

## Database Design

The `jobs` table stores:

* `id` – Primary key
* `name` – Job name
* `payload` – Arbitrary JSON payload
* `status` – Job status (`pending`, `completed`)
* `created_at` – Timestamp

SQLite is used for simplicity, but the schema is compatible with production databases like PostgreSQL or MySQL.

---

## Running the Project Locally

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn main:app --reload
```

### 4. Access the API

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Health check: [http://localhost:8000/health](http://localhost:8000/health)

---

## Design Decisions

* **Asynchronous job processing** to avoid blocking requests
* **Clear separation of layers** for maintainability
* **Explicit schema validation** using Pydantic
* **Proper HTTP status codes** for API correctness
* **Simple but realistic persistence layer**

---

## Possible Improvements

If this were a production system, the following enhancements would be considered:

* Retry mechanism for failed jobs
* Additional job states (`failed`, `retrying`)
* Pagination and filtering for job listings
* Authentication and authorization
* Structured logging and metrics
* Dockerization
* Automated tests

---

## Summary

This project demonstrates a clean and practical approach to building an asynchronous backend API using FastAPI. It focuses on real-world backend patterns, clear design decisions, and maintainable code structure, making it a solid foundation for scalable job-based systems.
