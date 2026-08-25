import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fast_wait = WebDriverWait(driver, 2.0)

    # Локаторы поиска
    NAV_SEARCH_TAB = (AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_search")
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia.alpha:id/search_card")
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    SEARCH_CLOSE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/search_close_btn")
    BOTTOM_SHEET = (AppiumBy.ID, "org.wikipedia.alpha:id/design_bottom_sheet")

    SEARCH_RESULT_TITLE = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'page_list_item_title') or contains(@resource-id, 'fragment_search_results')]//android.widget.TextView",
    )

    # Нижняя навигация
    NAV_HOME = (
        AppiumBy.XPATH,
        "//*[@resource-id='org.wikipedia.alpha:id/nav_tab_explore' or @content-desc='Home' or @content-desc='Explore']",
    )
    NAV_SAVED = (
        AppiumBy.XPATH,
        "//*[@resource-id='org.wikipedia.alpha:id/nav_tab_reading_lists' or @content-desc='Saved']",
    )
    NAV_MORE = (AppiumBy.ACCESSIBILITY_ID, "More")

    # Элементы открытых экранов
    SAVED_HEADER = (AppiumBy.XPATH, "//*[@text='Saved' or @text='All articles']")
    MORE_LOGIN_BUTTON = (AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_login_button")

    # Локаторы истории поиска
    CLEAR_HISTORY_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/history_delete")
    HISTORY_ITEM_TITLE = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")

    def _dismiss_popups(self):
        """Быстро закрывает известные модальные окна без задержек."""
        popups = [
            (AppiumBy.ID, "org.wikipedia.alpha:id/closeButton"),
            (AppiumBy.ACCESSIBILITY_ID, "Close")
        ]
        for locator in popups:
            elements = self.driver.find_elements(*locator)
            if elements and elements[0].is_displayed():
                elements[0].click()
                return

        for text in ["Got it", "GOT IT", "Got It", "Play", "Not now", "Skip"]:
            elements = self.driver.find_elements(AppiumBy.XPATH, f"//*[@text='{text}']")
            if elements and elements[0].is_displayed():
                elements[0].click()
                return

    @allure.step("Открытие экрана поиска")
    def open_search(self):
        """Устойчивое открытие поиска с циклом ретраев против лагов анимации Android."""
        end_time = time.time() + 15
        while time.time() < end_time:
            self._dismiss_popups()

            if self.driver.find_elements(*self.SEARCH_INPUT):
                return

            if self.driver.find_elements(*self.BOTTOM_SHEET):
                self.driver.back()
                time.sleep(0.3)
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

    @allure.step("Ввод поискового запроса: '{query}'")
    def type_search_query(self, query: str):
        self._dismiss_popups()
        search_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_field.click()
        search_field.clear()
        search_field.send_keys(query)

    @allure.step("Получение текста первого результата поиска")
    def get_first_result_text(self) -> str:
        self._dismiss_popups()
        result = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_TITLE)
        )
        return result.text

    @allure.step("Клик по первому результату поиска")
    def click_first_result(self):
        self._dismiss_popups()
        result = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_RESULT_TITLE)
        )
        result.click()

    @allure.step("Нажатие на кнопку очистки поиска (крестик)")
    def click_clear_search(self):
        clear_btn = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_CLOSE_BTN)
        )
        clear_btn.click()

    @allure.step("Получение текущего текста из поля ввода поиска")
    def get_search_input_text(self) -> str:
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        return search_input.text

    @allure.step("Переход на вкладку 'Home'")
    def open_home_tab(self):
        self._dismiss_popups()
        if self.driver.find_elements(*self.MORE_LOGIN_BUTTON) or self.driver.find_elements(*self.BOTTOM_SHEET):
            self.driver.back()

        self.wait.until(EC.element_to_be_clickable(self.NAV_HOME)).click()

    @allure.step("Переход на вкладку 'Saved'")
    def open_saved_tab(self):
        self._dismiss_popups()
        saved_btn = self.wait.until(EC.element_to_be_clickable(self.NAV_SAVED))
        saved_btn.click()

    @allure.step("Переход в меню 'More'")
    def open_more_tab(self):
        self._dismiss_popups()
        self.wait.until(EC.element_to_be_clickable(self.NAV_MORE)).click()

    @allure.step("Проверка отображения экрана 'Saved'")
    def is_saved_tab_displayed(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.SAVED_HEADER)).is_displayed()

    @allure.step("Проверка отображения меню 'More'")
    def is_more_menu_displayed(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.MORE_LOGIN_BUTTON)).is_displayed()

    @allure.step("Проверка наличия статьи '{title}' в списке сохраненных")
    def is_article_present_in_saved(self, title: str) -> bool:
        self.wait.until(EC.visibility_of_element_located(self.SAVED_HEADER))
        locator = (AppiumBy.XPATH, f"//*[contains(@text, '{title}')]")
        return len(self.driver.find_elements(*locator)) > 0

    @allure.step("Очистка всей истории поиска")
    def clear_search_history(self):
        clear_btn = self.wait.until(EC.element_to_be_clickable(self.CLEAR_HISTORY_BTN))
        clear_btn.click()

        confirm_locators = [
            (AppiumBy.ID, "android:id/button1"),
            (AppiumBy.XPATH, "//*[@text='OK' or @text='Clear' or @text='Удалить' or @text='Yes' or @text='Да']")
        ]

        for locator in confirm_locators:
            try:
                confirm_btn = self.fast_wait.until(EC.element_to_be_clickable(locator))
                confirm_btn.click()
                break
            except TimeoutException:
                pass

        time.sleep(0.5)

    @allure.step("Проверка наличия элемента '{title}' в истории поиска")
    def is_history_item_present(self, title: str) -> bool:
        locator = (AppiumBy.XPATH, f"//*[@resource-id='org.wikipedia.alpha:id/page_list_item_title' and @text='{title}']")
        try:
            return bool(self.fast_wait.until(EC.presence_of_element_located(locator)))
        except TimeoutException:
            return False