from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_button_link = Link(page, 'registration-page-login-link', 'Login button link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_button_link(self):
        self.login_button_link.click()
