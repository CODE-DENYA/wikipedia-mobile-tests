import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_save_article_to_list(driver, skip_onboarding):
    """Тест сохранения статьи в закладки (коллекции)."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    article_page.get_article_title()
    article_page.click_save_button()

    with allure.step("Проверка: отображается шторка добавления в коллекции"):
        assert article_page.is_save_sheet_displayed(), "Шторка сохранения статьи в коллекцию не появилась"