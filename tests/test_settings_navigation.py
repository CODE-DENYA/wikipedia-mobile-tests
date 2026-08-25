import allure
from pages.main_page import MainPage


@allure.epic("РќР°СЃС‚СЂРѕР№РєРё")
@allure.title("РџСЂРѕРІРµСЂРєР° РїРµСЂРµС…РѕРґР° РІ СЌРєСЂР°РЅ РќР°СЃС‚СЂРѕРµРє С‡РµСЂРµР· РјРµРЅСЋ More")
def test_navigate_to_settings(driver, skip_onboarding):
    """РЎС†РµРЅР°СЂРёР№: Р“Р»Р°РІРЅС‹Р№ СЌРєСЂР°РЅ -> РњРµРЅСЋ More -> РљР»РёРє РїРѕ Settings -> РџСЂРѕРІРµСЂРєР° Р·Р°РіРѕР»РѕРІРєР° Settings."""
    main_page = MainPage(driver)

    # 1. РџРµСЂРµС…РѕРґ РІ СЂР°Р·РґРµР» Settings РёР· РјРµРЅСЋ More
    main_page.open_settings()

    # 2. РџСЂРѕРІРµСЂРєР° РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ СЌРєСЂР°РЅР° РќР°СЃС‚СЂРѕРµРє
    with allure.step("РџСЂРѕРІРµСЂРєР°: РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ Р·Р°РіРѕР»РѕРІРѕРє 'Settings'"):
        assert main_page.is_settings_title_displayed(), "Р­РєСЂР°РЅ 'Settings' РЅРµ РѕС‚РєСЂС‹Р»СЃСЏ РёР»Рё Р·Р°РіРѕР»РѕРІРѕРє РЅРµ РЅР°Р№РґРµРЅ!"
