import allure
from pages.main_page import MainPage


def test_navigate_bottom_tabs(driver, skip_onboarding):
    """Тест переключения между табами нижнего меню (Saved, More, Home)."""
    main_page = MainPage(driver)

    main_page.open_saved_tab()
    with allure.step("Проверка: открылся экран 'Saved'"):
        assert main_page.is_saved_tab_displayed(), "Экран 'Saved' не отображается"

    main_page.open_more_tab()
    with allure.step("Проверка: открылось меню 'More'"):
        assert main_page.is_more_menu_displayed(), "Меню 'More' не отображается"

    main_page.open_home_tab()