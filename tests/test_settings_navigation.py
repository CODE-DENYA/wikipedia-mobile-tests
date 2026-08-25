import allure
from pages.main_page import MainPage


@allure.epic("Настройки")
@allure.title("Проверка перехода в экран Настроек через меню More")
def test_navigate_to_settings(driver, skip_onboarding):
    """Сценарий: Главный экран -> Меню More -> Клик по Settings -> Проверка заголовка Settings."""
    main_page = MainPage(driver)

    # 1. Переход в раздел Settings из меню More
    main_page.open_settings()

    # 2. Проверка отображения экрана Настроек
    with allure.step("Проверка: отображается заголовок 'Settings'"):
        assert main_page.is_settings_title_displayed(), "Экран 'Settings' не открылся или заголовок не найден!"