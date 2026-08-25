import allure
from pages.main_page import MainPage


@allure.epic("РџРѕРёСЃРє")
@allure.title("РџСЂРѕРІРµСЂРєР° СЃРѕРѕР±С‰РµРЅРёСЏ РїСЂРё РѕС‚СЃСѓС‚СЃС‚РІРёРё СЂРµР·СѓР»СЊС‚Р°С‚РѕРІ РїРѕРёСЃРєР°")
def test_search_no_results(driver, skip_onboarding):
    """РќРµРіР°С‚РёРІРЅС‹Р№ С‚РµСЃС‚: РІРІРѕРґ РЅРµСЃСѓС‰РµСЃС‚РІСѓСЋС‰РµР№ СЃС‚СЂРѕРєРё Рё РїСЂРѕРІРµСЂРєР° РЅР°РґРїРёСЃРё 'No results'."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("qwertyuiop12345")

    with allure.step("РџСЂРѕРІРµСЂРєР°: РЅР° СЌРєСЂР°РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ 'No results'"):
        assert main_page.is_no_results_displayed(), "РЎРѕРѕР±С‰РµРЅРёРµ 'No results' РЅРµ РїРѕСЏРІРёР»РѕСЃСЊ!"
