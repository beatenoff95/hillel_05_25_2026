# Homework 29.1. Dockerizate everything

Python application that calculates two numbers and saves the result to PostgreSQL.
Pytest tests verify the database connection and CRUD operations.

## Files

- `homework_29_1.py` - application code and database functions.
- `test_homework_29_1.py` - tests for PostgreSQL connection, insert, update, delete and select.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - application image.
- `docker-compose.yml` - PostgreSQL, application and test services.

## Docker Compose commands

Run all commands from the `lesson_29` directory.

Build the application image:

```bash
docker compose build
```

Run PostgreSQL and the application:

```bash
docker compose up app
```

Run PostgreSQL and tests inside Docker:

```bash
docker compose run --rm tests
```

Expected result:

```text
7 passed
```

## Cleanup

```bash
docker compose down -v
```
