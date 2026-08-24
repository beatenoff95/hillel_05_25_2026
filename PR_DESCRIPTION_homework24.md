# ДЗ 24.1. Cars API search

## Що зроблено

- Додано Flask API `cars_app.py` з endpoint-ами `/auth` та `/cars`.
- Реалізовано JWT-аутентифікацію через `HTTPBasicAuth`.
- Додано Pytest-тести для endpoint `/cars`.
- Первинну аутентифікацію організовано через fixture `scope="class"`.
- Для запитів використовується `requests.Session`.
- Тест параметризований на 7 наборів даних з різними `sort_by` і `limit`.
- Додано логування одночасно в консоль і файл `test_search.log`.

## Як перевірити

Встановити залежності:

```bash
pip install -r hillel_05_25_2026_homework24/lesson_24/requirements.txt
```

Запустити Flask API:

```bash
cd hillel_05_25_2026_homework24/lesson_24
python cars_app.py
```

В іншому терміналі запустити тести:

```bash
pytest hillel_05_25_2026_homework24/lesson_24/test_cars_search.py -s
```

## Результат перевірки

```text
7 passed in 0.22s
```
