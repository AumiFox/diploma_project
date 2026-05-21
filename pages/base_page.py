from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Базовый класс для всех Page Object моделей"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Открыть указанный URL"""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        """Найти несколько элементов с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator, timeout=10):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        return self.find_element(locator, timeout).text

    def is_element_visible(self, locator, timeout=5):
        """Проверить, видим ли элемент"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator, timeout=2):
        """Проверить, присутствует ли элемент в DOM"""
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def wait_for_url_change(self, old_url, timeout=10):
        """Ожидать смены URL"""
        return self.wait.until(lambda driver: driver.current_url != old_url)