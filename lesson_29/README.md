# Homework 29.1. Dockerizate everything

Python application that calculates two numbers and saves the result to PostgreSQL.
Pytest tests verify the database connection and CRUD operations.

## Files

- `homework_29_1.py` - application code and database functions.
- `test_homework_29_1.py` - tests for PostgreSQL connection, insert, update, delete and select.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - application image.

## Docker commands

Run all commands from the `lesson_29` directory.

```bash
docker network create homework29-network
```

```bash
docker run --name homework29-postgres \
  --network homework29-network \
  -e POSTGRES_DB=homework29 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 \
  -d postgres:16
```

```bash
docker build -t homework29-app .
```

Run the application:

```bash
docker run --rm \
  --network homework29-network \
  -e DATABASE_URL=postgresql://postgres:postgres@homework29-postgres:5432/homework29 \
  homework29-app
```

Run tests inside Docker:

```bash
docker run --rm \
  --network homework29-network \
  -e DATABASE_URL=postgresql://postgres:postgres@homework29-postgres:5432/homework29 \
  homework29-app pytest -v
```

Expected result:

```text
7 passed
```

## Cleanup

```bash
docker rm -f homework29-postgres
docker network rm homework29-network
```
