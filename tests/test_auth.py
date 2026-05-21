import pytest
from pages.auth_page import AuthPage
pytestmark = pytest.mark.nondestructive

class TestAuth:

    def test_auth_page_contains_all_tabs(self, browser, base_url):
        page = AuthPage(browser)
        page.open_auth_page()

        assert page.is_element_visible(page.PHONE_TAB)
        assert page.is_element_visible(page.EMAIL_TAB)
        assert page.is_element_visible(page.LOGIN_TAB)

    def test_valid_login_by_login(self, browser, account_login, valid_password):
        page = AuthPage(browser)
        page.open_auth_page()
        page.select_tab_by_login()
        page.enter_username(account_login)
        page.enter_password(valid_password)
        page.click_submit()

        assert page.is_redirected_to_lk()

    def test_valid_login_by_email(self, browser, account_email, valid_password):
        page = AuthPage(browser)
        page.open_auth_page()
        page.select_tab_by_email()
        page.enter_username(account_email)
        page.enter_password(valid_password)
        page.click_submit()

        assert page.is_redirected_to_lk()

    def test_invalid_password(self, browser, account_phone):
        page = AuthPage(browser)
        page.open_auth_page()
        page.select_tab_by_phone()
        page.enter_username(account_phone)
        page.enter_password("wrongpassword123")
        page.click_submit()

        error_text = page.get_error_message()
        assert "Неверный логин или пароль" in error_text or "ошибка" in error_text.lower()

    def test_empty_password(self, browser, account_phone):
        page = AuthPage(browser)
        page.open_auth_page()
        page.select_tab_by_phone()
        page.enter_username(account_phone)
        page.enter_password("")
        page.click_submit()

        assert "auth" in page.get_current_url() or "login" in page.get_current_url()

    def test_auto_tab_switch(self, browser):
        page = AuthPage(browser)
        page.open_auth_page()

        page.select_tab_by_phone()
        page.enter_username("test@mail.ru")

        active_tab = page.get_active_tab()
        assert "почт" in active_tab.lower() or "mail" in active_tab.lower()

    def test_register_link_visible(self, browser):
        page = AuthPage(browser)
        page.open_auth_page()

        assert page.is_element_visible(page.REGISTER_LINK)