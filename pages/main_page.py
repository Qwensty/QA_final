from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    SEARCH_BOX = (By.NAME, "kp_query")
    FILMS_MENU = (By.LINK_TEXT, "Фильмы")
    TOP_250_LINK = (By.CSS_SELECTOR, "a[href='/lists/movies/top250/']")
    PREMIERES_LINK = (By.LINK_TEXT, "Премьеры")
    SERIALS_LINK = (By.LINK_TEXT, "Сериалы")
    TOP_250_SERIALS_LINK = (By.CSS_SELECTOR, "a[href='/lists/movies/popular-series/']")

    def search_movie(self, movie_name):
        self.send_keys(self.SEARCH_BOX, movie_name)
        self.send_keys(self.SEARCH_BOX, Keys.RETURN)

    def open_films_menu(self):
        self.click(self.FILMS_MENU)

    def navigate_to_top_250(self):
        self.open_films_menu()
        self.click(self.TOP_250_LINK)

    def navigate_to_premieres(self):
        self.click(self.PREMIERES_LINK)

    def navigate_to_serials(self):
        self.click(self.SERIALS_LINK)

    def navigate_to_top_250_serials(self):
        self.navigate_to_serials()
        self.click(self.TOP_250_SERIALS_LINK)