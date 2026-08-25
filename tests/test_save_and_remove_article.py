import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.epic("РЎРѕС…СЂР°РЅРµРЅРЅРѕРµ")
@allure.title("РџСЂРѕРІРµСЂРєР° СЃРѕС…СЂР°РЅРµРЅРёСЏ Рё РѕС‚РјРµРЅС‹ СЃРѕС…СЂР°РЅРµРЅРёСЏ СЃС‚Р°С‚СЊРё С‡РµСЂРµР· С€С‚РѕСЂРєСѓ")
def test_save_and_remove_article(driver, skip_onboarding):
    """РЎС†РµРЅР°СЂРёР№: РџРѕРёСЃРє -> РћС‚РєСЂС‹С‚РёРµ -> Save -> РќР°Р¶Р°С‚РёРµ РЅР° 'Saved' РІ С€С‚РѕСЂРєРµ -> РџСЂРѕРІРµСЂРєР° РѕС‚СЃСѓС‚СЃС‚РІРёСЏ РІРѕ РІРєР»Р°РґРєРµ Saved."""
    main_page = MainPage(driver)
    article_page = ArticlePage(driver)
    search_query = "Appium"

    # 1. РџРѕРёСЃРє Рё РїРµСЂРµС…РѕРґ РІ СЃС‚Р°С‚СЊСЋ
    main_page.open_search()
    main_page.type_search_query(search_query)
    main_page.click_first_result()

    # 2. РЎРѕС…СЂР°РЅРµРЅРёРµ СЃС‚Р°С‚СЊРё (РѕС‚РєСЂС‹РІР°РµС‚ Bottom Sheet)
    article_page.click_save_button()

    with allure.step("РџСЂРѕРІРµСЂРєР°: РІ С€С‚РѕСЂРєРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ РёРєРѕРЅРєР° 'Saved'"):
        assert article_page.is_saved_bookmark_active(), "РРєРѕРЅРєР° 'Saved' РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ РІ С€С‚РѕСЂРєРµ!"

    # 3. РљР»РёРє РїРѕ Р·РЅР°С‡РєСѓ 'Saved' РІ С€С‚РѕСЂРєРµ РґР»СЏ РѕС‚РјРµРЅС‹ СЃРѕС…СЂР°РЅРµРЅРёСЏ
    article_page.click_saved_bookmark_in_sheet()

    # 4. Р’РѕР·РІСЂР°С‚ РЅР° РіР»Р°РІРЅС‹Р№ СЌРєСЂР°РЅ Рё РїРµСЂРµС…РѕРґ РІРѕ РІРєР»Р°РґРєСѓ Saved
    article_page.close_article_and_return_to_main()
    main_page.open_saved_tab()

    # 5. РџРѕРґС‚РІРµСЂР¶РґРµРЅРёРµ РѕС‚СЃСѓС‚СЃС‚РІРёСЏ СЃС‚Р°С‚СЊРё РІ СЃРїРёСЃРєРµ
    with allure.step(f"РџСЂРѕРІРµСЂРєР°: СЃС‚Р°С‚СЊСЏ '{search_query}' РѕС‚СЃСѓС‚СЃС‚РІСѓРµС‚ РІ СЃРїРёСЃРєРµ Saved"):
        assert not main_page.is_article_present_in_saved(search_query), f"РЎС‚Р°С‚СЊСЏ '{search_query}' РІСЃРµ РµС‰Рµ РІ Saved!"
