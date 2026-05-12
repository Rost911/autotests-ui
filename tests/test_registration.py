import pytest
from playwright.sync_api import  Page


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("user.name@gmail.com", "username", "password"),
        ("user2.name@gmail.com", "username4", "password2")
    ],
)
def test_successful_registration(
        registration_page: Page,
        dashboard_page: Page,
        email: str,
        username:str,
        password: str
) -> None:
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.fill_registration_form(email, username, password)

    registration_page.click_registration_button()

    dashboard_page.check_dashboard_title_visible()
