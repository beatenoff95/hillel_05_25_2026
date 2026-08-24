import logging
import sys
from pathlib import Path

import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"
LOG_FILE = Path(__file__).with_name("test_search.log")

CARS_DB = [
    {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
]


logger = logging.getLogger("cars_api_search")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def expected_cars(sort_by=None, limit=None):
    sort_key = sort_by or "brand"
    sorted_cars = sorted(CARS_DB, key=lambda car: car.get(sort_key, 0))
    return sorted_cars[:limit] if limit else sorted_cars


@pytest.fixture(scope="class")
def authenticated_session(request):
    session = requests.Session()

    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        timeout=5,
    )
    assert response.status_code == 200, response.text

    access_token = response.json()["access_token"]
    session.headers.update({"Authorization": "Bearer " + access_token})
    request.cls.session = session

    logger.info("Authentication succeeded for user '%s'", USERNAME)
    yield session
    session.close()


@pytest.mark.usefixtures("authenticated_session")
class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("brand", 5),
            ("price", 10),
            ("year", 7),
            ("engine_volume", 6),
            ("price", 3),
            ("year", 20),
            (None, 4),
        ],
    )
    def test_search_cars_with_sorting_and_limit(self, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info("GET /cars params=%s", params)
        response = self.session.get(f"{BASE_URL}/cars", params=params, timeout=5)
        logger.info(
            "Response status=%s count=%s",
            response.status_code,
            len(response.json()) if response.ok else "n/a",
        )

        assert response.status_code == 200
        assert response.json() == expected_cars(sort_by=sort_by, limit=limit)
