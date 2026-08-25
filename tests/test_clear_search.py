import allure
from pages.main_page import MainPage


def test_clear_search_query(driver, skip_onboarding):
    """РўРµСЃС‚ РѕС‡РёСЃС‚РєРё РІРІРµРґРµРЅРЅРѕРіРѕ Р·Р°РїСЂРѕСЃР° РїРѕ РєРЅРѕРїРєРµ 'РљСЂРµСЃС‚РёРє'."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("Appium")
    main_page.click_clear_search()

    current_text = main_page.get_search_input_text()
    print(f"\n[DEBUG] РўРµРєСЃС‚ РІ РїРѕР»Рµ РїРѕСЃР»Рµ РѕС‡РёСЃС‚РєРё: '{current_text}'")

    with allure.step("РџСЂРѕРІРµСЂРєР°: РїРѕР»Рµ РІРІРѕРґР° РїРѕРёСЃРєР° СЃР±СЂРѕС€РµРЅРѕ"):
        assert current_text in ["Search Wikipedia", "SearchвЂ¦", ""], \
            f"РћР¶РёРґР°Р»Рё СЃР±СЂРѕСЃ РїРѕР»СЏ РїРѕРёСЃРєР°, РЅРѕ РїРѕР»СѓС‡РёР»Рё: '{current_text}'"
