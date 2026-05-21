from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    """Страница авторизации"""

    # Локаторы
    TABS = {
        "phone": By.ID,  # ID элемента таба "Номер"
        "email": By.ID,  # ID элемента таба "Почта"
        "login": By.ID,  # ID элемента таба "Логин"
        "ls": By.ID  # ID элемента таба "Лицевой счет"
    }

    PHONE_TAB = (By.ID, "t-btn-tab-phone")
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    LS_TAB = (By.ID, "t-btn-tab-ls")

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "kc-login")

    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot-password")
    FORGOT_PASSWORD_COLOR = (By.CSS_SELECTOR, "#forgot-password.orange-color")

    REGISTER_LINK = (By.ID, "kc-register")
    AUTH_CODE_TAB = (By.ID, "t-btn-tab-otp")

    # Локаторы для авторизации по коду
    GET_CODE_BUTTON = (By.ID, "otp-get-code")
    CODE_INPUTS = (By.CSS_SELECTOR, ".rt-input__input")
    CHANGE_NUMBER_LINK = (By.CLASS_NAME, "otp-change-number")

    # Cookie popup
    COOKIE_POPUP = (By.CLASS_NAME, "cookie-modal")
    COOKIE_RETRY_BUTTON = (By.CLASS_NAME, "cookie-retry")

    def __init__(self, driver):
        super().__init__(driver)
        self.auth_url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid"

    def open_auth_page(self):
        """Открыть страницу авторизации"""
        self.open(self.auth_url)

    def select_tab_by_phone(self):
        """Выбрать таб авторизации по номеру телефона"""
        self.click(self.PHONE_TAB)

    def select_tab_by_email(self):
        """Выбрать таб авторизации по почте"""
        self.click(self.EMAIL_TAB)

    def select_tab_by_login(self):
        """Выбрать таб авторизации по логину"""
        self.click(self.LOGIN_TAB)

    def select_tab_by_ls(self):
        """Выбрать таб авторизации по лицевому счету"""
        self.click(self.LS_TAB)

    def select_auth_code_tab(self):
        """Выбрать таб авторизации по коду"""
        self.click(self.AUTH_CODE_TAB)

    def enter_username(self, username):
        """Ввести логин/телефон/почту"""
        self.input_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Ввести пароль"""
        self.input_text(self.PASSWORD_INPUT, password)

    def click_submit(self):
        """Нажать кнопку Войти"""
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        """Получить текст ошибки"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_forgot_password_orange(self):
        """Проверить, что ссылка 'Забыл пароль' оранжевая"""
        return self.is_element_visible(self.FORGOT_PASSWORD_COLOR)

    def click_forgot_password(self):
        """Кликнуть по ссылке 'Забыл пароль'"""
        self.click(self.FORGOT_PASSWORD_LINK)

    def click_register(self):
        """Кликнуть по ссылке 'Зарегистрироваться'"""
        self.click(self.REGISTER_LINK)

    def get_active_tab(self):
        """Получить активный таб"""
        active_tab = self.driver.find_element(By.CSS_SELECTOR, ".rt-tab-active")
        return active_tab.text

    def is_redirected_to_lk(self):
        """Проверить редирект в ЛК"""
        current_url = self.get_current_url()
        return "account_b2c" in current_url or "lk.smarthome" in current_url

    def is_cookie_popup_visible(self):
        """Проверить видимость popup о cookie"""
        return self.is_element_visible(self.COOKIE_POPUP, timeout=3)

    def click_cookie_retry(self):
        """Кликнуть по кнопке 'Повторить попытку'"""
        self.click(self.COOKIE_RETRY_BUTTON)

    # Методы для авторизации по коду
    def enter_phone_for_code(self, phone):
        """Ввести телефон для получения кода"""
        self.enter_username(phone)

    def click_get_code(self):
        """Нажать 'Получить код'"""
        self.click(self.GET_CODE_BUTTON)

    def is_code_inputs_visible(self):
        """Проверить, что поля для ввода кода отобразились"""
        return self.is_element_visible(self.CODE_INPUTS, timeout=5)

    def enter_code(self, code):
        """Ввести код подтверждения (6 цифр)"""
        code_inputs = self.find_elements(self.CODE_INPUTS)
        for i, digit in enumerate(str(code)):
            if i < len(code_inputs):
                code_inputs[i].send_keys(digit)

    def click_change_number(self):
        """Кликнуть 'Изменить номер'"""
        self.click(self.CHANGE_NUMBER_LINK)