from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)  # Увеличьте время ожидания до 30 секунд

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    def click(self, by_locator):
        element = self.find_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element.click()
        except Exception as e:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, by_locator, text):
        element = self.find_element(by_locator)
        element.send_keys(text)

    def get_text(self, by_locator):
        element = self.find_element(by_locator)
        return element.text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
