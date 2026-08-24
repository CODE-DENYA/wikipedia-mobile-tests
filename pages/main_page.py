import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Элементы навигации и поиска
    NAV_SEARCH_TAB = (AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_search")
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia.alpha:id/search_card")
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    SEARCH_CLOSE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/search_close_btn")
    BOTTOM_SHEET = (AppiumBy.ID, "org.wikipedia.alpha:id/design_bottom_sheet")

    # Результаты поиска
    SEARCH_RESULT_TITLE = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'page_list_item_title') or contains(@resource-id, 'fragment_search_results')]//android.widget.TextView",
    )

    def open_search(self):
        """Гарантированно переводит приложение в режим активного ввода поиска."""
        end_time = time.time() + 15
        while time.time() < end_time:
            if self.driver.find_elements(*self.SEARCH_INPUT):
                return

            if self.driver.find_elements(*self.BOTTOM_SHEET):
                self.driver.back()
                time.sleep(0.5)
                continue

            cards = self.driver.find_elements(*self.SEARCH_CARD)
            if cards:
                try:
                    cards[0].click()
                except Exception:
                    pass
                time.sleep(0.5)
                continue

            tabs = self.driver.find_elements(*self.NAV_SEARCH_TAB)
            if tabs:
                try:
                    tabs[0].click()
                except Exception:
                    pass
                time.sleep(0.5)
                continue

        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))

    def type_search_query(self, query: str):
        """Вводит текст в строку поиска."""
        search_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_field.click()
        search_field.clear()
        search_field.send_keys(query)

    def get_first_result_text(self) -> str:
        """Возвращает текст первого найденного элемента."""
        result = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_TITLE)
        )
        return result.text

    def click_first_result(self):
        """Кликает по первому результату в списке поиска."""
        result = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_RESULT_TITLE)
        )
        result.click()

    def click_clear_search(self):
        """Кликает по кнопке очистки поиска (крестик)."""
        clear_btn = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_CLOSE_BTN)
        )
        clear_btn.click()

    def get_search_input_text(self) -> str:
        """Возвращает текущий текст из поля ввода поиска."""
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        return search_input.text