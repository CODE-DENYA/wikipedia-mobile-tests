import time
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import config
from pages.onboarding_page import OnboardingPage


def pytest_addoption(parser):
    """Р РµРіРёСЃС‚СЂР°С†РёСЏ РєР°СЃС‚РѕРјРЅРѕРіРѕ С„Р»Р°РіР° --slow РґР»СЏ pytest."""
    parser.addoption(
        "--slow", action="store_true", help="Р—Р°РјРµРґР»РёС‚СЊ РІС‹РїРѕР»РЅРµРЅРёРµ С‚РµСЃС‚РѕРІ РґР»СЏ РІРёР·СѓР°Р»СЊРЅРѕРіРѕ РєРѕРЅС‚СЂРѕР»СЏ"
    )


@pytest.fixture(autouse=True)
def slow_mode(request, driver):
    """РђРІС‚РѕРјР°С‚РёС‡РµСЃРєР°СЏ РїР°СѓР·Р° РІ 1 СЃРµРєСѓРЅРґСѓ РїРµСЂРµРґ РєРѕРјР°РЅРґР°РјРё Appium РїСЂРё РїРµСЂРµРґР°С‡Рµ С„Р»Р°РіР° --slow."""
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

    # РћРїС‚РёРјРёР·Р°С†РёРё СЃРєРѕСЂРѕСЃС‚Рё СЂР°Р±РѕС‚С‹ Appium
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
    """Р“Р°СЂР°РЅС‚РёСЂРѕРІР°РЅРЅС‹Р№ РїСЂРѕРїСѓСЃРє РѕРЅР±РѕСЂРґРёРЅРіР° СЃ Р»СЋР±РѕРіРѕ РµРіРѕ СЌРєСЂР°РЅР°."""
    skip_buttons = driver.find_elements(
        AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button"
    ) or driver.find_elements(
        AppiumBy.XPATH, "//*[@text='Skip' or @text='РџР РћРџРЈРЎРўРРўР¬']"
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
    """РЎРЅСЏС‚РёРµ СЃРєСЂРёРЅС€РѕС‚Р° РїСЂРё СЃР±РѕРµ С‚РµСЃС‚Р° Рё РїСЂРёРєСЂРµРїР»РµРЅРёРµ Рє РѕС‚С‡С‘С‚Сѓ Allure."""
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
