import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("РЎС‚Р°С‚СЊРё")
@allure.title("РџСЂРѕРІРµСЂРєР° РїРѕСЏРІР»РµРЅРёСЏ РёРЅРґРёРєР°С‚РѕСЂР° 'Saved' РІ С€С‚РѕСЂРєРµ")
def test_article_saved_status_indicator(driver, skip_onboarding):
    """РџСЂРѕРІРµСЂРєР° РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ РёРєРѕРЅРєРё 'Saved' РІРѕ РІСЃРїР»С‹РІР°СЋС‰РµР№ С€С‚РѕСЂРєРµ РїРѕСЃР»Рµ СЃРѕС…СЂР°РЅРµРЅРёСЏ СЃС‚Р°С‚СЊРё."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    article_page.click_save_button()

    with allure.step("РџСЂРѕРІРµСЂРєР°: РІ С€С‚РѕСЂРєРµ СЃРѕС…СЂР°РЅРµРЅРёСЏ РїРѕСЏРІР»СЏРµС‚СЃСЏ РёРєРѕРЅРєР° 'Saved'"):
        assert article_page.is_saved_bookmark_active(), "РРЅРґРёРєР°С‚РѕСЂ 'Saved' РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ РІ С€С‚РѕСЂРєРµ!"
