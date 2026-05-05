from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_header = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_header).to_have_text("Courses")

    text_block = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_block).to_have_text("There is no results")

    icon_empty_block = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_empty_block).to_be_visible()

    text_block2 = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_block2).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )

