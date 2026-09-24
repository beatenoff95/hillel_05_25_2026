import os
import time

import psycopg


DATABASE_URL = os.environ["DATABASE_URL"]


def main() -> None:
    last_error = None

    for _ in range(30):
        try:
            with psycopg.connect(DATABASE_URL) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
            print("PostgreSQL is ready")
            return
        except psycopg.OperationalError as error:
            last_error = error
            time.sleep(1)

    raise RuntimeError("PostgreSQL did not become ready in time") from last_error


if __name__ == "__main__":
    main()
