from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_save_article_to_list(driver, skip_onboarding):
    """Тест сохранения статьи в закладки (коллекции)."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    # 1. Открываем поиск и вводим запрос
    main_page.open_search()
    main_page.type_search_query("Python")

    # 2. Переходим в статью
    main_page.click_first_result()
    article_page.get_article_title()

    # 3. Нажимаем кнопку Save
    article_page.click_save_button()

    # 4. Проверяем, что отобразилась шторка "Collect the articles you love"
    assert article_page.is_save_sheet_displayed(), "Шторка сохранения статьи в коллекцию не появилась"