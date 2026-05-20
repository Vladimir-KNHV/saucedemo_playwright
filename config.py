from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pydantic import FilePath, HttpUrl, DirectoryPath, BaseModel
from typing import Self

class Browser(str, Enum):
    WEBKIT = 'webkit'
    FIREFOX = 'firefox'
    CHROMIUM = 'chromium'

class TestUser(BaseModel):
    username: str
    password: str



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf8',
        env_nested_delimiter='.'
    )
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    videos_dir: DirectoryPath
    trace_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath('./videos')
        tracing_dir = DirectoryPath('./tracing')
        allure_results_dir = DirectoryPath('./allure-results')
        browser_state_file = FilePath("../saucedemo_playwright/browser-state.json")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            trace_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}"

settings = Settings.initialize()
