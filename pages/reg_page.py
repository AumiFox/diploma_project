from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegPage(BasePage):
    # ========== ЛОКАТОРЫ ==========

    # Кнопка регистрации на странице авторизации
    REGISTER_LINK = (By.ID, "kc-register")

    # Поля регистрации
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_OR_PHONE_INPUT = (By.NAME, "address")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_CONFIRM_INPUT = (By.NAME, "password-confirm")

    # Кнопка отправки (на странице регистрации)
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    # Регион (если есть)
    REGION_INPUT = (By.CSS_SELECTOR, ".rt-select__input.rt-input__input")

    # Ссылки
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(text(), 'политикой')]")
    USER_AGREEMENT_LINK = (By.XPATH, "//a[contains(text(), 'пользовательским')]")

    # ========== МЕТОДЫ ==========

    def open_reg_page(self):
        """Открыть страницу регистрации через кнопку на странице авторизации"""
        # Открываем страницу авторизации
        self.open(
            "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

        # Нажимаем кнопку "Зарегистрироваться"
        self.click(self.REGISTER_LINK)

    def enter_first_name(self, first_name):
        self.input_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.input_text(self.LAST_NAME_INPUT, last_name)

    def enter_email_or_phone(self, value):
        self.input_text(self.EMAIL_OR_PHONE_INPUT, value)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def enter_password_confirm(self, password):
        self.input_text(self.PASSWORD_CONFIRM_INPUT, password)

    def click_submit(self):
        """Нажать кнопку 'Зарегистрироваться'"""
        self.click(self.SUBMIT_BUTTON)

    def is_privacy_policy_visible(self):
        return self.is_element_visible(self.PRIVACY_POLICY_LINK)

    def is_user_agreement_visible(self):
        return self.is_element_visible(self.USER_AGREEMENT_LINK)

    # Вспомогательные методы для ошибок (если нужны)
    def get_first_name_error(self):
        error = (By.XPATH, "//input[@name='firstName']/following::span[contains(@class, 'error')]")
        return self.get_text(error) if self.is_element_present(error) else ""

    def get_last_name_error(self):
        error = (By.XPATH, "//input[@id='lastName']/following::span[contains(@class, 'error')]")
        return self.get_text(error) if self.is_element_present(error) else ""

    def get_password_error(self):
        error = (By.XPATH, "//input[@id='password']/following::span[contains(@class, 'error')]")
        return self.get_text(error) if self.is_element_present(error) else ""

    def get_confirm_error(self):
        error = (By.XPATH, "//input[@id='password-confirm']/following::span[contains(@class, 'error')]")
        return self.get_text(error) if self.is_element_present(error) else ""