import allure
from pages.main_page import MainPage


def test_search_article(driver, skip_onboarding):
    """Тест поиска статьи на Wikipedia."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")

    first_result = main_page.get_first_result_text()
    print(f"\n[DEBUG] Текст первого результата: '{first_result}'")

    with allure.step("Проверка: в первом результате поиска присутствует 'Python'"):
        assert "python" in first_result.lower(), f"Ожидалась подстрока 'Python', но получили: '{first_result}'"