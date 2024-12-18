import pytest
from utils.api_client import APIClient
import allure

@allure.feature("API Tests")
@pytest.mark.api
def test_get_random_movie():
    client = APIClient()
    with allure.step("Отправка запроса на получение случайного фильма"):
        response = client.get_random_movie()
    with allure.step("Проверка статус-кода ответа"):
        assert "id" in response, "Ответ не содержит ID фильма"


@allure.feature("API Tests")
@pytest.mark.api
def test_search_movie():
    client = APIClient()
    query = "Начало"
    with allure.step(f"Отправка запроса на поиск фильма по названию: {query}"):
        response = client.search_movie(query)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, "Статус ответа не 200"
    with allure.step("Проверка, что в ответе есть фильмы"):
        data = response.json()
        assert len(data.get("docs", [])) > 0, "Фильмы не найдены"


@allure.feature("API Tests")
@pytest.mark.api
def test_get_movie_by_id():
    client = APIClient()
    movie_id = 212840  # ID фильма для проверки
    with allure.step(f"Отправка запроса на получение фильма с ID: {movie_id}"):
        response = client.get_movie_by_id(movie_id)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, "Статус ответа не 200"
    with allure.step("Проверка содержимого ответа"):
        json_response = response.json()
        assert json_response.get("id") == movie_id, "ID фильма не совпадает"
        assert "title" in json_response or "alternativeName" in json_response, \
            "Ответ не содержит названия фильма или альтернативного названия"


@allure.feature("API Tests")
@pytest.mark.api
def test_filter_movies():
    client = APIClient()
    filters = {"type": "anime", "year": "2020-2024"}
    with allure.step(f"Отправка запроса с фильтрами: {filters}"):
        response = client.filter_movies(filters)
    with allure.step("Проверка содержимого ответа"):
        assert "docs" in response, "Ответ не содержит ключа 'docs'"
        assert len(response["docs"]) > 0, "Фильмы не найдены"


@allure.feature("API Tests")
@pytest.mark.api
def test_get_reviews():
    client = APIClient()
    movie_id = 1387128
    with allure.step(f"Отправка запроса на получение отзывов для фильма с ID: {movie_id}"):
        response = client.get_reviews(movie_id)
    with allure.step("Проверка содержимого ответа"):
        assert "docs" in response, "Ответ не содержит ключа 'docs'"
        assert len(response["docs"]) > 0, "Отзывы не найдены"


