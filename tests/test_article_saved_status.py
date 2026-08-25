import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("Статьи")
@allure.title("Проверка появления индикатора 'Saved' в шторке")
def test_article_saved_status_indicator(driver, skip_onboarding):
    """Проверка отображения иконки 'Saved' во всплывающей шторке после сохранения статьи."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    article_page.click_save_button()

    with allure.step("Проверка: в шторке сохранения появляется иконка 'Saved'"):
        assert article_page.is_saved_bookmark_active(), "Индикатор 'Saved' не отображается в шторке!"