import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticlePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Ищем элементы внутри WebView или нативные TextView, у которых text НЕ пустой
    ARTICLE_TITLE = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'page_title_text') or contains(@resource-id, 'view_page_header_text')] | "
        "//android.webkit.WebView//android.widget.TextView[string-length(@text) > 0] | "
        "//android.webkit.WebView//android.view.View[string-length(@text) > 0]"
    )

    # Точные селекторы для закрытия подсказок и тултипов
    POPUP_DISMISS_LOCATORS = [
        (AppiumBy.XPATH, "//*[@text='Got it' or @text='GOT IT' or @text='Got It']"),
        (AppiumBy.XPATH, "//*[contains(@text, 'GOT IT') or contains(@text, 'Got it') or contains(@text, 'ПОНЯТНО')]"),
        (AppiumBy.ID, "org.wikipedia.alpha:id/closeButton"),
    ]

    def _dismiss_popups(self):
        """Закрывает всплывающие подсказки (включая Customize your toolbar)."""
        for by, value in self.POPUP_DISMISS_LOCATORS:
            elements = self.driver.find_elements(by, value)
            if elements:
                try:
                    elements[0].click()
                    time.sleep(0.5)
                except Exception:
                    pass

    def get_article_title(self) -> str:
        """Считывает заголовок статьи, пропуская пустые контейнеры."""
        end_time = time.time() + 15
        while time.time() < end_time:
            self._dismiss_popups()

            elements = self.driver.find_elements(*self.ARTICLE_TITLE)
            for el in elements:
                text = el.text.strip()
                # Отсекаем служебные тексты и берем первый реальный заголовок
                if text and text not in ["Got it", "Customize your toolbar"]:
                    return text

            time.sleep(0.5)

        return self.wait.until(
            EC.visibility_of_element_located(self.ARTICLE_TITLE)
        ).text