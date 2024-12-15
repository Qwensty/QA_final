import requests
from config.settings import API_BASE_URL, API_KEY

class APIClient:
    def __init__(self):
        self.BASE_URL = API_BASE_URL
        self.session = requests.Session()
        # Добавляем обязательный заголовок
        self.session.headers.update({
            "X-API-KEY": API_KEY,
            "Accept": "application/json"
        })

    def get_random_movie(self):
        """Получить случайный фильм."""
        url = f"{self.BASE_URL}/v1.4/movie/random"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def search_movie(self, query: str):
        """Получить фильм по названию"""
        url = f"{self.BASE_URL}/v1.4/movie/search"
        params = {"query": query}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response

    def get_movie_by_id(self, movie_id):
        """Получить информацию о фильме по ID."""
        url = f"{self.BASE_URL}/v1.4/movie/{movie_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return response

    def filter_movies(self, filters):
        """Фильтрация фильмов по параметрам."""
        url = f"{self.BASE_URL}/v1.4/movie"
        response = self.session.get(url, params=filters)
        response.raise_for_status()
        return response.json()

    def get_reviews(self, movie_id):
        """Получение отзывов пользователей по фильму."""
        url = f"{self.BASE_URL}/v1.4/review"
        params = {"movieId": movie_id, "page": 1, "limit": 10}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

