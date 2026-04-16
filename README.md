# 📚 Book Tracker API

![CI Pipeline](https://github.com/oyarifa74/book-tracker-api/actions/workflows/ci.yml/badge.svg)

## 🛠️ Tech Stack

- **Python 3.11**
- **Flask** — Web framework
- **PostgreSQL 15** — Database
- **SQLAlchemy** — ORM
- **Docker & Docker Compose** — Containerization

## 🚀 How to Run

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Steps
1. Clone the repository:
```bash
   git clone https://github.com/YOUR_USERNAME/book-tracker-api.git
   cd book-tracker-api
```

2. Create a `.env` file:
3. Build and run:
```bash
   docker-compose up --build
```

4. API is running at `http://localhost:5000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/<id>` | Get a single book |
| POST | `/books` | Add a new book |
| PUT | `/books/<id>` | Update a book |
| DELETE | `/books/<id>` | Delete a book |

## 📝 Example Request

```bash
curl -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "The Pragmatic Programmer", "author": "David Thomas", "year": 2019, "read": false}'
```

## 📂 Project Structure