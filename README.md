# HTTP Metadata Inventory Service

## Overview

This project is a FastAPI-based HTTP Metadata Inventory Service developed as part of the CloudSEK SDE 1 Hiring Challenge.

The service:

* Fetches website metadata from a given URL
* Extracts headers, cookies, and HTML page source
* Stores metadata in MongoDB
* Supports asynchronous background metadata collection
* Runs using Docker Compose

---

# Tech Stack

* Python 3.11
* FastAPI
* MongoDB
* Motor (Async MongoDB Driver)
* Docker Compose
* httpx
* Pytest

---

# Features

* POST endpoint to collect and store metadata
* GET endpoint to retrieve stored metadata
* Asynchronous background processing
* MongoDB integration
* Dockerized environment
* Swagger/OpenAPI documentation

---

# Project Structure

```text
metadata-inventory-service
│
├── app
│   ├── routes
│   ├── services
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── tests
│   └── test_api.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

# Prerequisites

Before running the project, install:

* Docker Desktop
* Git
* VS Code (optional)

---

# Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Example:

```bash
git clone https://github.com/yourusername/http-metadata-inventory-service.git
```

---

# Move Into Project Folder

```bash
cd http-metadata-inventory-service
```

---

# Run Project Using Docker

Make sure Docker Desktop is running.

Run:

```bash
docker-compose up --build
```

This command:

* builds FastAPI container
* starts MongoDB container
* connects services automatically

---

# API Documentation

Open browser:

```text
http://localhost:8000/docs
```

Swagger UI provides:

* API testing
* request/response schemas
* endpoint documentation

---

# Health Check API

## GET /

Response:

```json
{
  "status": "healthy"
}
```

---

# POST Endpoint

## POST /metadata

### Request Body

```json
{
  "url": "https://example.com"
}
```

### Functionality

This endpoint:

* receives URL
* fetches metadata
* extracts headers, cookies, and page source
* stores data in MongoDB

### Sample Response

```json
{
  "message": "Metadata stored successfully"
}
```

---

# GET Endpoint

## GET /metadata

### Example

```text
GET /metadata?url=https://example.com
```

### Workflow

* checks MongoDB for metadata
* returns metadata if available
* triggers async background collection if missing

### First Response Example

```json
{
  "status": 202,
  "message": "Metadata collection started in background"
}
```

### Subsequent Response Example

```json
{
  "message": "Metadata found"
}
```

---

# Run Tests

```bash
pytest
```

---

# Stop Containers

```bash
docker-compose down
```

---

# Design Decisions

* FastAPI used for asynchronous API development
* MongoDB used for flexible metadata storage
* Async background processing implemented using asyncio.create_task()
* Docker Compose used for environment consistency
* MongoDB indexing added on URL field for optimized lookup

---

# Future Improvements

* Retry mechanism
* Rate limiting
* Authentication
* Redis queue integration
* Celery workers
* Distributed processing

---

# Author

Ganesh Naik
