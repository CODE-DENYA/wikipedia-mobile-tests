import os
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.onboarding_page import OnboardingPage


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_dir, "app", "wikipedia.apk")

    options.app = app_path
    options.app_package = "org.wikipedia.alpha"
    options.app_activity = "org.wikipedia.main.MainActivity"

    # Оптимизации скорости работы Appium
    options.skip_logcat_capture = True
    options.disable_window_animation = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(0)

    yield driver

    driver.quit()


@pytest.fixture
def onboarding_page(driver):
    return OnboardingPage(driver)


@pytest.fixture
def skip_onboarding(driver, onboarding_page):
    """Гарантированный пропуск онбординга с любого его экрана."""
    skip_buttons = driver.find_elements(
        AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button"
    ) or driver.find_elements(
        AppiumBy.XPATH, "//*[@text='Skip' or @text='ПРОПУСТИТЬ']"
    )

    if skip_buttons:
        try:
            skip_buttons[0].click()
            return
        except Exception:
            pass

    if onboarding_page.is_primary_text_displayed():
        onboarding_page.complete_onboarding()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Снятие скриншота при сбое теста и прикрепление к отчёту Allure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )