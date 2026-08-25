import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("Сохраненное")
@allure.title("Проверка сохранения и отмены сохранения статьи через шторку")
def test_save_and_remove_article(driver, skip_onboarding):
    """Сценарий: Поиск -> Открытие -> Save -> Нажатие на 'Saved' в шторке -> Проверка отсутствия во вкладке Saved."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)
    search_query = "Appium"

    # 1. Поиск и переход в статью
    main_page.open_search()
    main_page.type_search_query(search_query)
    main_page.click_first_result()

    # 2. Сохранение статьи (открывает Bottom Sheet)
    article_page.click_save_button()

    with allure.step("Проверка: в шторке отображается иконка 'Saved'"):
        assert article_page.is_saved_bookmark_active(), "Иконка 'Saved' не отображается в шторке!"

    # 3. Клик по значку 'Saved' в шторке для отмены сохранения
    article_page.click_saved_bookmark_in_sheet()

    # 4. Возврат на главный экран и переход во вкладку Saved
    article_page.close_article_and_return_to_main()
    main_page.open_saved_tab()

    # 5. Подтверждение отсутствия статьи в списке
    with allure.step(f"Проверка: статья '{search_query}' отсутствует в списке Saved"):
        assert not main_page.is_article_present_in_saved(search_query), f"Статья '{search_query}' все еще в Saved!"