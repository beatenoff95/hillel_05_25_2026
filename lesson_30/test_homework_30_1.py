from decimal import Decimal

import allure
import pytest

from homework_30_1 import (
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
    with allure.step("Create calculation_results table if it does not exist"):
        init_db()

    with allure.step("Clean calculation_results table before test"):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE calculation_results RESTART IDENTITY")

    yield

    with allure.step("Clean calculation_results table after test"):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE calculation_results RESTART IDENTITY")


@allure.feature("Calculation results storage")
class TestCalculationResultsStorage:
    def test_database_connection(self):
        with allure.step("Open PostgreSQL connection and execute health query"):
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1 AS status")
                    row = cursor.fetchone()

        with allure.step("Verify database returns expected health status"):
            assert row["status"] == 1

    def test_insert_result(self):
        with allure.step("Insert calculation result"):
            saved_result = create_result("2 + 3", Decimal("5"))

        with allure.step("Verify inserted result fields"):
            assert saved_result.id == 1
            assert saved_result.expression == "2 + 3"
            assert saved_result.result == Decimal("5")

    def test_select_result_by_id(self):
        with allure.step("Create calculation result for selection"):
            saved_result = create_result("10 / 2", Decimal("5"))

        with allure.step("Select calculation result by id"):
            selected_result = get_result(saved_result.id)

        with allure.step("Verify selected result matches saved result"):
            assert selected_result == saved_result

    def test_select_all_results(self):
        with allure.step("Create two calculation results"):
            first_result = create_result("4 * 5", Decimal("20"))
            second_result = create_result("9 - 3", Decimal("6"))

        with allure.step("Select all calculation results"):
            results = list_results()

        with allure.step("Verify all results are returned in id order"):
            assert results == [first_result, second_result]

    def test_update_result(self):
        with allure.step("Create calculation result for update"):
            saved_result = create_result("1 + 1", Decimal("2"))

        with allure.step("Update calculation result"):
            updated_result = update_result(saved_result.id, "2 + 2", Decimal("4"))

        with allure.step("Verify updated result fields"):
            assert updated_result.id == saved_result.id
            assert updated_result.expression == "2 + 2"
            assert updated_result.result == Decimal("4")

    def test_delete_result(self):
        with allure.step("Create calculation result for deletion"):
            saved_result = create_result("7 - 2", Decimal("5"))

        with allure.step("Delete calculation result"):
            is_deleted = delete_result(saved_result.id)

        with allure.step("Verify result was deleted"):
            assert is_deleted is True
            assert get_result(saved_result.id) is None

    def test_calculate_and_save_result(self):
        with allure.step("Calculate expression result"):
            expression, result = calculate(Decimal("8"), Decimal("4"), "/")

        with allure.step("Save calculated result to PostgreSQL"):
            saved_result = create_result(expression, result)

        with allure.step("Verify saved calculated result"):
            assert saved_result.expression == "8 / 4"
            assert saved_result.result == Decimal("2")
