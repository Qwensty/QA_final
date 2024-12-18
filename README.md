## Проект для автоматизации тестирования сайта Кинопоиск.

## Проект организован в следующей структуре:
```plaintext
QA_final/
├── config/
│   ├── settings.py         # Настройки окружения
├── pages/                  # PageObject-классы
│   ├── __init__.py
│   ├── base_page.py        # Базовый класс для всех страниц
│   ├── main_page.py        # Главная страница
│   
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── test_ui.py          # UI-тесты
│   ├── test_api.py         # API-тесты
├── utils/                  # Утилиты
│   ├── api_client.py       # Работа с API
│   
├── requirements.txt        # Зависимости проекта
├── pytest.ini              # Настройка pytest
├── README.md               # Описание проекта
```
## Установка
1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`.

## Запуск тестов
- UI тесты: `pytest -m ui`
- API тесты: `pytest -m api`
- Все тесты: `pytest`

## Отчеты Allure
1. Запустите тесты: `pytest --alluredir=allure-results`.
2. Просмотрите отчет: `allure serve allure-results`.