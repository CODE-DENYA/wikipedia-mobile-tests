import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_save_article_to_list(driver, skip_onboarding):
    """E2E-тест сохранения статьи в закладки и проверки её наличия в разделе Saved."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    # 1. Находим и открываем статью
    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    # 2. Получаем заголовок (гарантированно закрывает тултип-подсказку)
    article_title = article_page.get_article_title()

    # 3. Сохраняем статью
    article_page.click_save_button()
    with allure.step("Проверка: отображается шторка сохранения"):
        assert article_page.is_save_sheet_displayed(), "Шторка сохранения не появилась"

    # 4. Закрываем все шторки и возвращаемся на главный экран
    article_page.close_article_and_return_to_main()

    # 5. Переходим на вкладку Saved и проверяем наличие статьи
    main_page.open_saved_tab()

    with allure.step(f"Проверка: статья '{article_title}' присутствует в разделе Saved"):
        assert main_page.is_article_present_in_saved("Python"), "Статья 'Python' не найдена в списке Saved"