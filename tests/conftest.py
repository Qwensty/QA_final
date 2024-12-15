import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Инициализирует драйвер для тестов."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()