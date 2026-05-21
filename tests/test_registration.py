import pytest
from pages.reg_page import RegPage

pytestmark = pytest.mark.nondestructive


class TestRegistration:

    def test_registration_page_elements(self, browser):
        """TC-01: Проверка наличия элементов на форме регистрации"""
        page = RegPage(browser)
        page.open_reg_page()

        assert page.is_element_visible(page.FIRST_NAME_INPUT)
        assert page.is_element_visible(page.LAST_NAME_INPUT)
        assert page.is_element_visible(page.EMAIL_OR_PHONE_INPUT)
        assert page.is_element_visible(page.PASSWORD_INPUT)
        assert page.is_element_visible(page.PASSWORD_CONFIRM_INPUT)
        assert page.is_element_visible(page.SUBMIT_BUTTON)

    def test_valid_first_name(self, browser):
        """TC-04: Валидное имя (кириллица, тире)"""
        page = RegPage(browser)
        page.open_reg_page()
        page.enter_first_name("Анна-Мария")
        page.click_submit()

        error = page.get_first_name_error()
        assert error == "", f"Ожидалась отсутствие ошибки, но получено: {error}"

    def test_invalid_first_name(self, browser):
        """TC-05: Невалидное имя (менее 2 символов)"""
        page = RegPage(browser)
        page.open_reg_page()
        page.enter_first_name("А")
        page.click_submit()

        error = page.get_first_name_error()
        assert error != "", "Ожидалась ошибка валидации имени"

    def test_password_too_short(self, browser):
        """TC-07: Пароль менее 8 символов"""
        page = RegPage(browser)
        page.open_reg_page()
        page.enter_first_name("Иван")
        page.enter_last_name("Иванов")
        page.enter_email_or_phone("test@test.ru")
        page.enter_password("Qwe1")
        page.enter_password_confirm("Qwe1")
        page.click_submit()

        error = page.get_password_error()
        assert error != "", "Ожидалась ошибка о длине пароля"

    def test_passwords_do_not_match(self, browser):
        """TC-10: Пароли не совпадают"""
        page = RegPage(browser)
        page.open_reg_page()
        page.enter_first_name("Иван")
        page.enter_last_name("Иванов")
        page.enter_email_or_phone("test@test.ru")
        page.enter_password("Qwerty123")
        page.enter_password_confirm("Qwerty124")
        page.click_submit()

        error = page.get_confirm_error()
        assert error != "", "Ожидалась ошибка о несовпадении паролей"

    def test_privacy_policy_link_visible(self, browser):
        """Проверка ссылки на политику конфиденциальности"""
        page = RegPage(browser)
        page.open_reg_page()

        assert page.is_privacy_policy_visible(), "Ссылка на политику не найдена"