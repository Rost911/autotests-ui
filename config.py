# config.py
from enum import Enum
from typing import Self, List

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: List[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    # Added initialize method
    @classmethod
    def initialize(cls) -> Self:  # Returns an instance of the Settings class
        # Define paths
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")
        browser_state_file = FilePath("browser-state.json")

        # Create directories if they don't exist
        videos_dir.mkdir(exist_ok=True)  # Ignore the error if the directory already exists
        allure_results_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)

        # Create the browser state file if it doesn't exist
        browser_state_file.touch(exist_ok=True)  # Ignore the error if the file already exists

        # Return the settings model with initialized values
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file,
        )

settings = Settings.initialize()