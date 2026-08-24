import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_open_article(driver, skip_onboarding):
    """Тест перехода в статью из результатов поиска."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    article_title = article_page.get_article_title()
    print(f"\n[DEBUG] Заголовок открытой статьи: '{article_title}'")

    with allure.step("Проверка: заголовок статьи содержит 'Python'"):
        assert "python" in article_title.lower(), f"Ожидали 'Python' в заголовке статьи, но получили: '{article_title}'"