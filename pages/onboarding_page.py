import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OnboardingPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(0)
        self.wait = WebDriverWait(driver, 3)

    PRIMARY_TEXT = (
        AppiumBy.XPATH,
        "//*[contains(@text, 'All the world') or contains(@text, 'Free encyclopedia')]",
    )

    FORWARD_BTN = (AppiumBy.ACCESSIBILITY_ID, "Forward")
    NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Next")
    DONE_BTN = (AppiumBy.ACCESSIBILITY_ID, "Get started")

    @allure.step("РџСЂРѕРІРµСЂРєР° РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ РїРµСЂРІРѕРіРѕ СЌРєСЂР°РЅР° РѕРЅР±РѕСЂРґРёРЅРіР°")
    def is_primary_text_displayed(self) -> bool:
        """Р‘РµР·РѕРїР°СЃРЅР°СЏ РїСЂРѕРІРµСЂРєР° РЅР°Р»РёС‡РёСЏ РїРµСЂРІРѕРіРѕ СЌРєСЂР°РЅР° РѕРЅР±РѕСЂРґРёРЅРіР°."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.PRIMARY_TEXT)
            ).is_displayed()
        except TimeoutException:
            return False

    @allure.step("РњРіРЅРѕРІРµРЅРЅРѕРµ РїСЂРѕС…РѕР¶РґРµРЅРёРµ РѕРЅР±РѕСЂРґРёРЅРіР°")
    def complete_onboarding(self):
        """РњРіРЅРѕРІРµРЅРЅРѕРµ РїСЂРѕС…РѕР¶РґРµРЅРёРµ РѕРЅР±РѕСЂРґРёРЅРіР° С‡РµСЂРµР· РїСЂРѕРІРµСЂРѕС‡РЅС‹Рµ РєР»РёРєРё."""
        for _ in range(8):
            if self._click_if_present(self.FORWARD_BTN):
                continue

            if self._click_if_present(self.NEXT_BTN):
                continue

            if self._click_if_present(self.DONE_BTN):
                break

            break

    def _click_if_present(self, locator) -> bool:
        """Р‘С‹СЃС‚СЂС‹Р№ РєР»РёРє Р±РµР· РїР°РґРµРЅРёСЏ РїРѕ С‚Р°Р№РјР°СѓС‚Сѓ."""
        try:
            elements = self.driver.find_elements(*locator)
            if elements and elements[0].is_displayed():
                elements[0].click()
                return True
        except Exception:
            pass
        return False
