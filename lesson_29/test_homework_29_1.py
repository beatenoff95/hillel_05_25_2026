from decimal import Decimal

import pytest

from homework_29_1 import (
    calculate,
    create_result,
    delete_result,
    get_connection,
    get_result,
    init_db,
    list_results,
    update_result,
)


@pytest.fixture(autouse=True)
def clean_database():
    init_db()

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE calculation_results RESTART IDENTITY")

    yield

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE calculation_results RESTART IDENTITY")


def test_database_connection():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 AS status")
            row = cursor.fetchone()

    assert row["status"] == 1


def test_insert_result():
    saved_result = create_result("2 + 3", Decimal("5"))

    assert saved_result.id == 1
    assert saved_result.expression == "2 + 3"
    assert saved_result.result == Decimal("5")


def test_select_result_by_id():
    saved_result = create_result("10 / 2", Decimal("5"))

    selected_result = get_result(saved_result.id)

    assert selected_result == saved_result


def test_select_all_results():
    first_result = create_result("4 * 5", Decimal("20"))
    second_result = create_result("9 - 3", Decimal("6"))

    assert list_results() == [first_result, second_result]


def test_update_result():
    saved_result = create_result("1 + 1", Decimal("2"))

    updated_result = update_result(saved_result.id, "2 + 2", Decimal("4"))

    assert updated_result.id == saved_result.id
    assert updated_result.expression == "2 + 2"
    assert updated_result.result == Decimal("4")


def test_delete_result():
    saved_result = create_result("7 - 2", Decimal("5"))

    assert delete_result(saved_result.id) is True
    assert get_result(saved_result.id) is None


def test_calculate_and_save_result():
    expression, result = calculate(Decimal("8"), Decimal("4"), "/")
    saved_result = create_result(expression, result)

    assert saved_result.expression == "8 / 4"
    assert saved_result.result == Decimal("2")
