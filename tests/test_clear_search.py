import allure
from pages.main_page import MainPage


def test_clear_search_query(driver, skip_onboarding):
    """Тест очистки введенного запроса по кнопке 'Крестик'."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("Appium")
    main_page.click_clear_search()

    current_text = main_page.get_search_input_text()
    print(f"\n[DEBUG] Текст в поле после очистки: '{current_text}'")

    with allure.step("Проверка: поле ввода поиска сброшено"):
        assert current_text in ["Search Wikipedia", "Search…", ""], \
            f"Ожидали сброс поля поиска, но получили: '{current_text}'"