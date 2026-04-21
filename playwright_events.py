from playwright.sync_api import sync_playwright, Request, Response


# Request logging
def log_request(request: Request):
    print(f"Request: {request.url}")


# Response logging
def log_response(response: Response):
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    # Open the browser and create a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Add event handlers
    page.on("request", log_request)   # Request sent
    page.on("response", log_response)  # Response received

    # Navigate to the login page
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Delay to complete all requests
    page.wait_for_timeout(3000)