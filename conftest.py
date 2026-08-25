import time
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import config
from pages.onboarding_page import OnboardingPage


def pytest_addoption(parser):
    """Регистрация кастомного флага --slow для pytest."""
    parser.addoption(
        "--slow", action="store_true", help="Замедлить выполнение тестов для визуального контроля"
    )


@pytest.fixture(autouse=True)
def slow_mode(request, driver):
    """Автоматическая пауза в 1 секунду перед командами Appium при передаче флага --slow."""
    if request.config.getoption("--slow"):
        original_execute = driver.execute

        def slow_execute(driver_command, params=None):
            time.sleep(1.0)
            return original_execute(driver_command, params)

        driver.execute = slow_execute


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = config.DEVICE_NAME

    options.app = config.APP_PATH
    options.app_package = config.APP_PACKAGE
    options.app_activity = config.APP_ACTIVITY

    # Оптимизации скорости работы Appium
    options.skip_logcat_capture = True
    options.disable_window_animation = True

    driver = webdriver.Remote(config.APPIUM_URL, options=options)
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