import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file():
    # Do nothing before the test session starts
    yield  # Run the test suite...
    # Create the environment.properties file after the test session completes
    create_allure_environment_file()