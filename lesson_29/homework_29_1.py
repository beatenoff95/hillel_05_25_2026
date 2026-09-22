import argparse
import os
import time
from dataclasses import dataclass
from decimal import Decimal

import psycopg
from psycopg.rows import dict_row


DEFAULT_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/homework29"


@dataclass(frozen=True)
class CalculationResult:
    id: int
    expression: str
    result: Decimal


def get_database_url() -> str:
    return os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)


def get_connection(retries: int = 10, delay: float = 1.0):
    last_error = None

    for _ in range(retries):
        try:
            return psycopg.connect(get_database_url(), row_factory=dict_row)
        except psycopg.OperationalError as error:
            last_error = error
            time.sleep(delay)

    raise RuntimeError("Could not connect to PostgreSQL") from last_error


def init_db() -> None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS calculation_results (
                    id SERIAL PRIMARY KEY,
                    expression TEXT NOT NULL,
                    result NUMERIC NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )


def create_result(expression: str, result: Decimal | int | float | str) -> CalculationResult:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO calculation_results (expression, result)
                VALUES (%s, %s)
                RETURNING id, expression, result
                """,
                (expression, Decimal(str(result))),
            )
            row = cursor.fetchone()

    return CalculationResult(**row)


def get_result(result_id: int) -> CalculationResult | None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, expression, result
                FROM calculation_results
                WHERE id = %s
                """,
                (result_id,),
            )
            row = cursor.fetchone()

    return CalculationResult(**row) if row else None


def list_results() -> list[CalculationResult]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, expression, result
                FROM calculation_results
                ORDER BY id
                """
            )
            rows = cursor.fetchall()

    return [CalculationResult(**row) for row in rows]


def update_result(result_id: int, expression: str, result: Decimal | int | float | str) -> CalculationResult | None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE calculation_results
                SET expression = %s, result = %s
                WHERE id = %s
                RETURNING id, expression, result
                """,
                (expression, Decimal(str(result)), result_id),
            )
            row = cursor.fetchone()

    return CalculationResult(**row) if row else None


def delete_result(result_id: int) -> bool:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM calculation_results WHERE id = %s",
                (result_id,),
            )
            deleted_rows = cursor.rowcount

    return deleted_rows == 1


def calculate(first_number: Decimal, second_number: Decimal, operator: str) -> tuple[str, Decimal]:
    operations = {
        "+": lambda: first_number + second_number,
        "-": lambda: first_number - second_number,
        "*": lambda: first_number * second_number,
        "/": lambda: first_number / second_number,
    }

    if operator not in operations:
        raise ValueError("Operator must be one of: +, -, *, /")

    expression = f"{first_number} {operator} {second_number}"
    return expression, operations[operator]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate two numbers and save the result to PostgreSQL.")
    parser.add_argument("first_number", type=Decimal)
    parser.add_argument("operator", choices=["+", "-", "*", "/"])
    parser.add_argument("second_number", type=Decimal)
    args = parser.parse_args()

    init_db()
    expression, result = calculate(args.first_number, args.second_number, args.operator)
    saved_result = create_result(expression, result)

    print(f"Saved result #{saved_result.id}: {saved_result.expression} = {saved_result.result}")


if __name__ == "__main__":
    main()
