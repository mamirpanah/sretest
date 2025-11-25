# GeoIP Flask API

A simple Flask-based API that detects the country of incoming requests, logs them into a PostgreSQL database, and supports Alembic migrations.

## Features

- **Flask REST API**
- **GeoIP lookup** using `geoip2`
- **PostgreSQL storage** via SQLAlchemy
- **Database schema migrations** via Alembic
- **Docker-ready structure**

## Project Structure

```
sretest/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── models.py
│   └── migrations/
│       ├── env.py
│       ├── versions/
│       └── script.py.mako
├── alembic.ini
├── requirements.txt
└── README.md
```

## Installation

1. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate it**

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Database Setup

Edit `alembic.ini`:

```ini
sqlalchemy.url = postgresql+psycopg://USER:PASSWORD@HOST:PORT/DBNAME
```

## Running Migrations

- **For the first time to create migrations:**
  ```bash
  alembic init migrations
  ```

- **Generate migration:**
  ```bash
  alembic revision --autogenerate -m "create request_logs table"
  ```

- **Apply migration:**
  ```bash
  alembic upgrade head
  ```

## Run the API

```bash
python app.py
```

The API will start at:

[http://localhost:8080/api/country](http://localhost:8080/api/country)