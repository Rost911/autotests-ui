from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Open the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Wait for the page to fully load
    )

    # Execute JS code to replace the title text
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    # Add pause for visual demonstration
    page.wait_for_timeout(5000)