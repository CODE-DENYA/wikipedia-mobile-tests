import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticlePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    ARTICLE_TITLE = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'page_title_text') or contains(@resource-id, 'view_page_header_text')] | "
        "//android.webkit.WebView//android.widget.TextView[string-length(@text) > 0] | "
        "//android.webkit.WebView//android.view.View[string-length(@text) > 0]",
    )

    SAVE_BUTTON = (AppiumBy.ID, "org.wikipedia.alpha:id/page_save")
    SAVE_BOTTOM_SHEET = (
        AppiumBy.XPATH,
        "//*[@resource-id='org.wikipedia.alpha:id/design_bottom_sheet'] | //*[contains(@text, 'Collect the articles')]",
    )
    SAVED_SHEET_BOOKMARK = (AppiumBy.ACCESSIBILITY_ID, "Saved")
    NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def _dismiss_popups(self):
        """Гарантированно уничтожает всплывающие окна и рекламные модалки на странице статьи."""
        try:
            close_btn = WebDriverWait(self.driver, 1.0).until(
                EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/closeButton"))
            )
            close_btn.click()
            time.sleep(0.5)
            return
        except Exception:
            pass

        try:
            close_by_desc = WebDriverWait(self.driver, 0.8).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Close"))
            )
            close_by_desc.click()
            time.sleep(0.5)
            return
        except Exception:
            pass

        for text in ["Got it", "GOT IT", "Got It", "Play", "Not now", "Skip"]:
            try:
                btn = self.driver.find_elements(AppiumBy.XPATH, f"//*[@text='{text}']")
                if btn:
                    btn[0].click()
                    time.sleep(0.5)
                    break
            except Exception:
                pass

    @allure.step("Получение заголовка статьи")
    def get_article_title(self) -> str:
        """Считывает заголовок статьи."""
        end_time = time.time() + 15
        while time.time() < end_time:
            self._dismiss_popups()

            elements = self.driver.find_elements(*self.ARTICLE_TITLE)
            for el in elements:
                text = el.text.strip()
                if text and text not in ["Got it", "Customize your toolbar", "Introducing Wikipedia games"]:
                    return text

            time.sleep(0.5)

        return self.wait.until(
            EC.visibility_of_element_located(self.ARTICLE_TITLE)
        ).text

    @allure.step("Клик по кнопке 'Save'")
    def click_save_button(self):
        """Кликает по кнопке Save на нижней панели статьи."""
        self._dismiss_popups()
        save_btn = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        save_btn.click()

    @allure.step("Проверка отображения шторки сохранения")
    def is_save_sheet_displayed(self) -> bool:
        """Проверяет появление шторки добавления в коллекции."""
        try:
            return bool(
                self.wait.until(
                    EC.visibility_of_element_located(self.SAVE_BOTTOM_SHEET)
                )
            )
        except Exception:
            return False

    @allure.step("Проверка наличия активного индикатора 'Saved' в шторке")
    def is_saved_bookmark_active(self) -> bool:
        """Проверяет появление зелёной иконки/закладки Saved во всплывающей шторке."""
        try:
            return bool(
                self.wait.until(
                    EC.visibility_of_element_located(self.SAVED_SHEET_BOOKMARK)
                )
            )
        except Exception:
            return False

    @allure.step("Клик по значку 'Saved' во всплывающей шторке")
    def click_saved_bookmark_in_sheet(self):
        """Нажимает на иконку Saved в шторке для отмены сохранения статьи."""
        bookmark = self.wait.until(
            EC.element_to_be_clickable(self.SAVED_SHEET_BOOKMARK)
        )
        bookmark.click()

    @allure.step("Закрытие статьи и возврат на главный экран")
    def close_article_and_return_to_main(self):
        """Выходит из статьи и режима поиска на главный экран."""
        end_time = time.time() + 12
        while time.time() < end_time:
            self._dismiss_popups()
            if self.driver.find_elements(AppiumBy.ID, "org.wikipedia.alpha:id/main_nav_tab_container"):
                return

            nav_buttons = self.driver.find_elements(*self.NAVIGATE_UP)
            if nav_buttons:
                try:
                    nav_buttons[0].click()
                except Exception:
                    self.driver.back()
            else:
                self.driver.back()

            time.sleep(0.8)