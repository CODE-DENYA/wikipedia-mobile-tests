import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


def test_save_article_to_list(driver, skip_onboarding):
    """E2E-С‚РµСЃС‚ СЃРѕС…СЂР°РЅРµРЅРёСЏ СЃС‚Р°С‚СЊРё РІ Р·Р°РєР»Р°РґРєРё Рё РїСЂРѕРІРµСЂРєРё РµС‘ РЅР°Р»РёС‡РёСЏ РІ СЂР°Р·РґРµР»Рµ Saved."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)

    # 1. РќР°С…РѕРґРёРј Рё РѕС‚РєСЂС‹РІР°РµРј СЃС‚Р°С‚СЊСЋ
    main_page.open_search()
    main_page.type_search_query("Python")
    main_page.click_first_result()

    # 2. РџРѕР»СѓС‡Р°РµРј Р·Р°РіРѕР»РѕРІРѕРє (РіР°СЂР°РЅС‚РёСЂРѕРІР°РЅРЅРѕ Р·Р°РєСЂС‹РІР°РµС‚ С‚СѓР»С‚РёРї-РїРѕРґСЃРєР°Р·РєСѓ)
    article_title = article_page.get_article_title()

    # 3. РЎРѕС…СЂР°РЅСЏРµРј СЃС‚Р°С‚СЊСЋ
    article_page.click_save_button()
    with allure.step("РџСЂРѕРІРµСЂРєР°: РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ С€С‚РѕСЂРєР° СЃРѕС…СЂР°РЅРµРЅРёСЏ"):
        assert article_page.is_save_sheet_displayed(), "РЁС‚РѕСЂРєР° СЃРѕС…СЂР°РЅРµРЅРёСЏ РЅРµ РїРѕСЏРІРёР»Р°СЃСЊ"

    # 4. Р—Р°РєСЂС‹РІР°РµРј РІСЃРµ С€С‚РѕСЂРєРё Рё РІРѕР·РІСЂР°С‰Р°РµРјСЃСЏ РЅР° РіР»Р°РІРЅС‹Р№ СЌРєСЂР°РЅ
    article_page.close_article_and_return_to_main()

    # 5. РџРµСЂРµС…РѕРґРёРј РЅР° РІРєР»Р°РґРєСѓ Saved Рё РїСЂРѕРІРµСЂСЏРµРј РЅР°Р»РёС‡РёРµ СЃС‚Р°С‚СЊРё
    main_page.open_saved_tab()

    with allure.step(f"РџСЂРѕРІРµСЂРєР°: СЃС‚Р°С‚СЊСЏ '{article_title}' РїСЂРёСЃСѓС‚СЃС‚РІСѓРµС‚ РІ СЂР°Р·РґРµР»Рµ Saved"):
        assert main_page.is_article_present_in_saved("Python"), "РЎС‚Р°С‚СЊСЏ 'Python' РЅРµ РЅР°Р№РґРµРЅР° РІ СЃРїРёСЃРєРµ Saved"
