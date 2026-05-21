from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResetPage(BasePage):
    """Страница восстановления пароля"""

    # Локаторы
    RESET_TABS = {
        "phone": (By.ID, "t-btn-tab-phone"),
        "email": (By.ID, "t-btn-tab-mail"),
        "login": (By.ID, "t-btn-tab-login"),
        "ls": (By.ID, "t-btn-tab-ls")
    }

    USERNAME_INPUT = (By.ID, "username")
    CAPTCHA_INPUT = (By.ID, "captcha")
    NEXT_BUTTON = (By.ID, "next-button")
    BACK_BUTTON = (By.ID, "back-button")

    # Форма выбора способа восстановления
    SMS_OPTION = (By.XPATH, "//button[contains(text(),'По SMS')]")
    EMAIL_OPTION = (By.XPATH, "//button[contains(text(),'По ссылке на почту')]")
    CONTINUE_RESET_BUTTON = (By.ID, "continue-reset")

    # Форма ввода кода
    CODE_INPUTS = (By.CSS_SELECTOR, ".rt-input__input")
    RESEND_CODE_BUTTON = (By.XPATH, "//button[contains(text(),'Получить код повторно')]")
    BACK_TO_USERNAME_BUTTON = (By.XPATH, "//button[contains(text(),'Вернуться назад')]")
    CODE_ERROR = (By.CLASS_NAME, "code-error")

    # Форма ввода нового пароля
    NEW_PASSWORD_INPUT = (By.ID, "new-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm-password")
    SAVE_BUTTON = (By.ID, "save-button")

    # Ошибки пароля
    PASSWORD_LENGTH_ERROR = (By.XPATH, "//*[contains(text(),'Длина пароля должна быть не менее 8 символов')]")
    PASSWORD_UPPERCASE_ERROR = (By.XPATH, "//*[contains(text(),'хотя бы одну заглавную букву')]")
    PASSWORD_LATIN_ERROR = (By.XPATH, "//*[contains(text(),'только латинские буквы')]")
    PASSWORD_MISMATCH_ERROR = (By.XPATH, "//*[contains(text(),'Пароли не совпадают')]")
    PASSWORD_USED_ERROR = (By.XPATH, "//*[contains(text(),'пароль уже использовался')]")

    def open_reset_page(self):
        """Открыть страницу восстановления пароля"""
        self.open("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials")

    def select_reset_tab(self, tab_name):
        """Выбрать таб восстановления"""
        if tab_name in self.RESET_TABS:
            self.click(self.RESET_TABS[tab_name])

    def enter_username(self, username):
        """Ввести телефон/почту/логин/ЛС"""
        self.input_text(self.USERNAME_INPUT, username)

    def enter_captcha(self, captcha_code):
        """Ввести капчу (в реальных тестах нужно решать)"""
        self.input_text(self.CAPTCHA_INPUT, captcha_code)

    def click_next(self):
        """Нажать 'Далее'"""
        self.click(self.NEXT_BUTTON)

    def click_back(self):
        """Нажать 'Вернуться'"""
        self.click(self.BACK_BUTTON)

    def select_sms_option(self):
        """Выбрать восстановление по SMS"""
        self.click(self.SMS_OPTION)

    def select_email_option(self):
        """Выбрать восстановление по почте"""
        self.click(self.EMAIL_OPTION)

    def click_continue_reset(self):
        """Нажать 'Продолжить'"""
        self.click(self.CONTINUE_RESET_BUTTON)

    def is_code_form_visible(self):
        """Проверить видимость формы ввода кода"""
        return self.is_element_visible(self.CODE_INPUTS, timeout=5)

    def enter_reset_code(self, code):
        """Ввести код из SMS/письма"""
        code_inputs = self.find_elements(self.CODE_INPUTS)
        for i, digit in enumerate(str(code)):
            if i < len(code_inputs):
                code_inputs[i].send_keys(digit)

    def click_resend_code(self):
        """Кликнуть 'Получить код повторно'"""
        self.click(self.RESEND_CODE_BUTTON)

    def click_back_to_username(self):
        """Кликнуть 'Вернуться назад'"""
        self.click(self.BACK_TO_USERNAME_BUTTON)

    def get_code_error(self):
        """Получить ошибку ввода кода"""
        return self.get_text(self.CODE_ERROR) if self.is_element_present(self.CODE_ERROR) else ""

    def enter_new_password(self, password):
        """Ввести новый пароль"""
        self.input_text(self.NEW_PASSWORD_INPUT, password)

    def enter_confirm_password(self, password):
        """Ввести подтверждение пароля"""
        self.input_text(self.CONFIRM_PASSWORD_INPUT, password)

    def click_save(self):
        """Нажать 'Сохранить'"""
        self.click(self.SAVE_BUTTON)

    def get_password_length_error(self):
        """Получить ошибку длины пароля"""
        return self.is_element_visible(self.PASSWORD_LENGTH_ERROR)

    def get_password_uppercase_error(self):
        """Получить ошибку о заглавной букве"""
        return self.is_element_visible(self.PASSWORD_UPPERCASE_ERROR)

    def get_password_latin_error(self):
        """Получить ошибку о латинских буквах"""
        return self.is_element_visible(self.PASSWORD_LATIN_ERROR)

    def get_password_mismatch_error(self):
        """Получить ошибку несовпадения паролей"""
        return self.is_element_visible(self.PASSWORD_MISMATCH_ERROR)

    def is_redirected_to_auth(self):
        """Проверить редирект на страницу авторизации"""
        current_url = self.get_current_url()
        return "auth" in current_url or "login" in current_url