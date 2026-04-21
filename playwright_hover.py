from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Open the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Find the Registration link
    registration_link = page.get_by_test_id('login-page-registration-link')

    # Hover over the link
    registration_link.hover()

    # Add pause for visual demonstration
    page.wait_for_timeout(5000)