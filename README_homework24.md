# hillel_05_25_2026_homework24

## ДЗ 24.1. Cars API search

У папці `lesson_24` знаходиться Flask API для пошуку автомобілів та Pytest-тести для перевірки endpoint `/cars`.

### Файли

- `cars_app.py` - серверна частина Flask API.
- `test_cars_search.py` - параметризовані Pytest-тести через `requests.Session`.
- `requirements.txt` - залежності для запуску.
- `test_search.log` - файл логів тестового запуску.

### Встановлення залежностей

```bash
pip install -r lesson_24/requirements.txt
```

### Запуск Flask API

```bash
cd lesson_24
python cars_app.py
```

API буде доступне за адресою `http://127.0.0.1:8080`.

### Запуск тестів

В іншому терміналі:

```bash
pytest lesson_24/test_cars_search.py -s
```

Тести використовують:

- `requests.Session`;
- `HTTPBasicAuth`;
- fixture `scope="class"` для первинної аутентифікації;
- `pytest.mark.parametrize` з 7 наборами `sort_by` і `limit`;
- логування в консоль і файл `lesson_24/test_search.log`.
