import allure
import pytest
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("История поиска")
class TestSearchHistory:

    @allure.title("Проверка сохранения запроса в историю и его очистки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_history_flow(self, driver, skip_onboarding):
        main_page = MainPage(driver)
        article_page = ArticlePage(driver)

        # 1. Открываем поиск, вводим запрос и переходим в статью
        main_page.open_search()
        main_page.type_search_query("Python")
        main_page.click_first_result()

        # 2. Возвращаемся со страницы статьи обратно (история уже перед глазами)
        article_page.close_article_and_return_to_main()

        # 3. Сразу проверяем наличие «Python» в истории без лишних поисков инпута
        assert main_page.is_history_item_present("Python"), "Статья не найдена в истории поиска!"

        # 4. Очищаем историю поиска
        main_page.clear_search_history()

        # 5. Проверяем, что история пуста
        assert not main_page.is_history_item_present("Python"), "История поиска не была очищена!"