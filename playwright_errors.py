from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Open the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Try to verify that a non-existing locator is visible on the page
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Try to enter text into the Login button
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Try to change the title text
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)