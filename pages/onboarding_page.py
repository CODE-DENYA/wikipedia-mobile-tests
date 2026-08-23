from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OnboardingPage:

    def __init__(self, driver):
        self.driver = driver
        # Если в conftest стоял implicitly_wait, обнуляем его
        self.driver.implicitly_wait(0)
        self.wait = WebDriverWait(driver, 3)

    PRIMARY_TEXT = (
        AppiumBy.XPATH,
        "//*[contains(@text, 'All the world') or contains(@text, 'Free encyclopedia')]",
    )

    # Быстрые локаторы по Accessibility ID (content-desc)
    FORWARD_BTN = (AppiumBy.ACCESSIBILITY_ID, "Forward")
    NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Next")
    DONE_BTN = (AppiumBy.ACCESSIBILITY_ID, "Get started")

    def is_primary_text_displayed(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self.PRIMARY_TEXT)
        ).is_displayed()

    def complete_onboarding(self):
        """Мгновенное прохождение онбординга через проверочные клики."""
        for _ in range(8):
            # Пробуем кликнуть Forward
            if self._click_if_present(self.FORWARD_BTN):
                continue

            # Пробуем кликнуть Next
            if self._click_if_present(self.NEXT_BTN):
                continue

            # Пробуем кликнуть Get started (финиш)
            if self._click_if_present(self.DONE_BTN):
                break

            break

    def _click_if_present(self, locator) -> bool:
        """Быстрый клик без долгих таймаутов."""
        try:
            elements = self.driver.find_elements(*locator)
            if elements and elements[0].is_displayed():
                elements[0].click()
                return True
        except Exception:
            pass
        return False