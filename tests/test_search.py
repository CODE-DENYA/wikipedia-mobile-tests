from pages.main_page import MainPage


def test_search_article(driver, skip_onboarding):
    """Тест поиска статьи на Wikipedia."""
    main_page = MainPage(driver)

    # 1. Переходим в поиск и активируем строку
    main_page.open_search()

    # 2. Вводим запрос
    main_page.type_search_query("Python")

    # 3. Получаем текст первого результата
    first_result = main_page.get_first_result_text()

    # Для отладки: печатаем, что реально прочитал тест
    print(f"\n[DEBUG] Текст первого результата: '{first_result}'")

    # 4. Проверяем (assert), что в заголовке присутствует "Python" (без учета регистра)
    assert "python" in first_result.lower(), f"Ожидалось подстрока 'Python', но получили: '{first_result}'"