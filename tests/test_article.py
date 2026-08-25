import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_open_article(driver, skip_onboarding):
    """РўРµСЃС‚ РїРµСЂРµС…РѕРґР° РІ СЃС‚Р°С‚СЊСЋ РёР· СЂРµР·СѓР»СЊС‚Р°С‚РѕРІ РїРѕРёСЃРєР°."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    article_title = article_page.get_article_title()
    print(f"\n[DEBUG] Р—Р°РіРѕР»РѕРІРѕРє РѕС‚РєСЂС‹С‚РѕР№ СЃС‚Р°С‚СЊРё: '{article_title}'")

    with allure.step("РџСЂРѕРІРµСЂРєР°: Р·Р°РіРѕР»РѕРІРѕРє СЃС‚Р°С‚СЊРё СЃРѕРґРµСЂР¶РёС‚ 'Python'"):
        assert "python" in article_title.lower(), f"РћР¶РёРґР°Р»Рё 'Python' РІ Р·Р°РіРѕР»РѕРІРєРµ СЃС‚Р°С‚СЊРё, РЅРѕ РїРѕР»СѓС‡РёР»Рё: '{article_title}'"
