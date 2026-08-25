import allure
from pages.main_page import MainPage


@allure.epic("Поиск")
@allure.title("Проверка сообщения при отсутствии результатов поиска")
def test_search_no_results(driver, skip_onboarding):
    """Негативный тест: ввод несуществующей строки и проверка надписи 'No results'."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("qwertyuiop12345")

    with allure.step("Проверка: на экране отображается 'No results'"):
        assert main_page.is_no_results_displayed(), "Сообщение 'No results' не появилось!"