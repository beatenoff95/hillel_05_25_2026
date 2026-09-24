# Homework 30.1. Allure for PostgreSQL tests

Python application that calculates two numbers and saves the result to PostgreSQL.
Pytest tests use Allure decorators and steps.

## Files

- `homework_30_1.py` - application code and database functions.
- `test_homework_30_1.py` - tests with `allure.feature` and `allure.step`.
- `requirements.txt` - Python dependencies.
- `Dockerfile` - application image.
- `docker-compose.yml` - PostgreSQL, application and test services.

## Docker Compose commands

Run all commands from the `lesson_30` directory.

Build the application image:

```bash
docker compose build
```

Run PostgreSQL and the application:

```bash
docker compose up app
```

Run PostgreSQL and tests with Allure results:

```bash
docker compose run --rm tests
```

The command writes Allure result files to `lesson_30/allure-results`.

Expected result:

```text
7 passed
```

## Cleanup

```bash
docker compose down -v
```
