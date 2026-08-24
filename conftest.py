import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.onboarding_page import OnboardingPage


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"

    # Абсолютный путь к APK относительно файла conftest.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_dir, "app", "wikipedia.apk")

    options.app = app_path
    options.app_package = "org.wikipedia.alpha"
    options.app_activity = "org.wikipedia.main.MainActivity"

    # Подключаемся к Appium Server
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(0)

    yield driver

    # Завершаем сессию после каждого теста
    driver.quit()


@pytest.fixture
def onboarding_page(driver):
    """Фикстура для создания экземпляра страницы онбординга."""
    return OnboardingPage(driver)


@pytest.fixture
def skip_onboarding(onboarding_page):
    """
    Предусловие (Precondition):
    Если открыт онбординг, автоматически проходим его,
    чтобы функциональный тест сразу стартовал с главного экрана.
    """
    if onboarding_page.is_primary_text_displayed():
        onboarding_page.complete_onboarding()