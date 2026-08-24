from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_open_article(driver, skip_onboarding):
    """Тест перехода в статью из результатов поиска."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    # 1. Открываем поиск и вводим запрос
    main_page.open_search()
    main_page.type_search_query("Python")

    # 2. Кликаем по первому результату
    main_page.click_first_result()

    # 3. Проверяем заголовок открытой статьи
    article_title = article_page.get_article_title()
    print(f"\n[DEBUG] Заголовок открытой статьи: '{article_title}'")

    assert "python" in article_title.lower(), f"Ожидали 'Python' в заголовке статьи, но получили: '{article_title}'"