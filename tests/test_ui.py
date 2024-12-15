import pytest
from selenium.webdriver.common.keys import Keys
from config.settings import BASE_URL
from pages.main_page import MainPage
import allure

@allure.step("Открыть главную страницу")
def open_main_page(driver):
    driver.get(BASE_URL)

@allure.title("Тест поиска фильма")
def test_search_movie(driver):
    open_main_page(driver)
    main_page = MainPage(driver)
    main_page.search_movie("Inception")
    assert "Inception" in driver.page_source

@allure.title("Тест перехода на страницу Топ-250")
def test_navigate_to_top_250(driver):
    open_main_page(driver)
    main_page = MainPage(driver)
    main_page.navigate_to_top_250()
    assert "250 лучших фильмов" in driver.page_source

@allure.title("Тест перехода на страницу Премьеры")
def test_navigate_to_premieres(driver):
    open_main_page(driver)
    main_page = MainPage(driver)
    main_page.navigate_to_premieres()
    assert "Премьеры" in driver.page_source

@allure.title("Тест перехода на страницу Сериалы")
def test_navigate_to_serials(driver):
    open_main_page(driver)
    main_page = MainPage(driver)
    main_page.navigate_to_serials()
    assert "Сериалы" in driver.page_source

@allure.title("Тест перехода на страницу Топ-250 сериалов")
def test_navigate_to_top_250_serials(driver):
    open_main_page(driver)
    main_page = MainPage(driver)
    main_page.navigate_to_top_250_serials()
    assert "250 лучших сериалов" in driver.page_source

