from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Open the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Set focus on the Email field
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # Simulate key presses character by character to enter text
    for character in 'user@gmail.com':
        # Add 300 ms delay to imitate real typing
        page.keyboard.press(character, delay=300)

    # Select all text in the Email field using Ctrl+A shortcut
    page.keyboard.press("ControlOrMeta+A")

    # Wait 5 seconds for visual demonstration
    page.wait_for_timeout(5000)