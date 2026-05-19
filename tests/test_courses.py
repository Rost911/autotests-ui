from playwright.sync_api import  expect, Page
import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

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

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage) -> None:
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()

    create_course_page.check_disabled_create_course_button()

    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    create_course_page.check_visible_exercises_title()

    create_course_page.check_visible_create_exercise_button()

    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")

    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()

    courses_list_page.check_visible_create_course_button()

    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )




