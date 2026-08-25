import allure
from pages.main_page import MainPage


def test_navigate_bottom_tabs(driver, skip_onboarding):
    """РўРµСЃС‚ РїРµСЂРµРєР»СЋС‡РµРЅРёСЏ РјРµР¶РґСѓ С‚Р°Р±Р°РјРё РЅРёР¶РЅРµРіРѕ РјРµРЅСЋ (Saved, More, Home)."""
    main_page = MainPage(driver)

    main_page.open_saved_tab()
    with allure.step("РџСЂРѕРІРµСЂРєР°: РѕС‚РєСЂС‹Р»СЃСЏ СЌРєСЂР°РЅ 'Saved'"):
        assert main_page.is_saved_tab_displayed(), "Р­РєСЂР°РЅ 'Saved' РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ"

    main_page.open_more_tab()
    with allure.step("РџСЂРѕРІРµСЂРєР°: РѕС‚РєСЂС‹Р»РѕСЃСЊ РјРµРЅСЋ 'More'"):
        assert main_page.is_more_menu_displayed(), "РњРµРЅСЋ 'More' РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ"

    main_page.open_home_tab()
