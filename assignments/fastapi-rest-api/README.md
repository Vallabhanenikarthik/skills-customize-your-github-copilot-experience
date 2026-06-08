# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small RESTful API using the FastAPI framework to practice defining endpoints, request/response models, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Implement a CRUD API for `items`

#### Description
Build a FastAPI application that exposes endpoints to create, read, update, and delete simple `item` records. Use Pydantic models for request/response validation and keep the storage in-memory for simplicity.

#### Requirements
Completed project should:

- Expose the following endpoints:
  - `GET /items` — list all items
  - `GET /items/{id}` — retrieve a single item
  - `POST /items` — create a new item
  - `PUT /items/{id}` — update an existing item
  - `DELETE /items/{id}` — delete an item
- Use Pydantic models for input validation and response schemas.
- Return appropriate HTTP status codes (e.g., `201` for create, `404` for not found).
- Include simple in-memory storage (a Python list) so the API is runnable without a database.
- Provide clear run instructions in this `README`.

#### Example

```
# Create an item
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"name":"apple","description":"A tasty fruit"}'

# List items
curl http://localhost:8000/items
```

### 🛠️ Optional Enhancements

#### Description
Add one or more enhancements to make the API more realistic or feature-complete.

#### Requirements (pick any)

- Persist items to a simple SQLite database using SQLAlchemy.
- Add pagination or filtering to `GET /items`.
- Add basic authentication (API key or token) for write endpoints.
- Add automated tests for endpoints using `pytest` and `httpx`.

## 🚀 Run locally

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app with Uvicorn:

```bash
uvicorn starter_app.main:app --reload --host 127.0.0.1 --port 8000
```

3. Open `http://127.0.0.1:8000/docs` to explore the auto-generated API docs.
