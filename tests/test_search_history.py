import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("РСЃС‚РѕСЂРёСЏ РїРѕРёСЃРєР°")
class TestSearchHistory:

    @allure.title("РџСЂРѕРІРµСЂРєР° СЃРѕС…СЂР°РЅРµРЅРёСЏ Р·Р°РїСЂРѕСЃР° РІ РёСЃС‚РѕСЂРёСЋ Рё РµРіРѕ РѕС‡РёСЃС‚РєРё")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_history_flow(self, driver, skip_onboarding):
        main_page = MainPage(driver)
        article_page = ArticlePage(driver)

        # 1. РћС‚РєСЂС‹РІР°РµРј РїРѕРёСЃРє, РІРІРѕРґРёРј Р·Р°РїСЂРѕСЃ Рё РїРµСЂРµС…РѕРґРёРј РІ СЃС‚Р°С‚СЊСЋ
        main_page.open_search()
        main_page.type_search_query("Python")
        main_page.click_first_result()

        # 2. Р’РѕР·РІСЂР°С‰Р°РµРјСЃСЏ СЃРѕ СЃС‚СЂР°РЅРёС†С‹ СЃС‚Р°С‚СЊРё РѕР±СЂР°С‚РЅРѕ (РёСЃС‚РѕСЂРёСЏ СѓР¶Рµ РїРµСЂРµРґ РіР»Р°Р·Р°РјРё)
        article_page.close_article_and_return_to_main()

        # 3. РЎСЂР°Р·Сѓ РїСЂРѕРІРµСЂСЏРµРј РЅР°Р»РёС‡РёРµ В«PythonВ» РІ РёСЃС‚РѕСЂРёРё Р±РµР· Р»РёС€РЅРёС… РїРѕРёСЃРєРѕРІ РёРЅРїСѓС‚Р°
        assert main_page.is_history_item_present("Python"), "РЎС‚Р°С‚СЊСЏ РЅРµ РЅР°Р№РґРµРЅР° РІ РёСЃС‚РѕСЂРёРё РїРѕРёСЃРєР°!"

        # 4. РћС‡РёС‰Р°РµРј РёСЃС‚РѕСЂРёСЋ РїРѕРёСЃРєР°
        main_page.clear_search_history()

        # 5. РџСЂРѕРІРµСЂСЏРµРј, С‡С‚Рѕ РёСЃС‚РѕСЂРёСЏ РїСѓСЃС‚Р°
        assert not main_page.is_history_item_present("Python"), "РСЃС‚РѕСЂРёСЏ РїРѕРёСЃРєР° РЅРµ Р±С‹Р»Р° РѕС‡РёС‰РµРЅР°!"
