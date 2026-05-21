import pytest
from pages.reset_page import ResetPage
pytestmark = pytest.mark.nondestructive

class TestPasswordReset:

    def test_reset_page_elements(self, browser):
        page = ResetPage(browser)
        page.open_reset_page()

        assert page.is_element_visible(page.RESET_TABS["phone"])
        assert page.is_element_visible(page.RESET_TABS["email"])
        assert page.is_element_visible(page.USERNAME_INPUT)

    def test_back_button_on_first_step(self, browser):
        page = ResetPage(browser)
        page.open_reset_page()
        page.click_back()

        assert "auth" in page.get_current_url() or "login" in page.get_current_url()