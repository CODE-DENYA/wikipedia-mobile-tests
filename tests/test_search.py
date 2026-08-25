import allure
from pages.main_page import MainPage


def test_search_article(driver, skip_onboarding):
    """РўРµСЃС‚ РїРѕРёСЃРєР° СЃС‚Р°С‚СЊРё РЅР° Wikipedia."""
    main_page = MainPage(driver)

    main_page.open_search()
    main_page.type_search_query("Python")

    first_result = main_page.get_first_result_text()
    print(f"\n[DEBUG] РўРµРєСЃС‚ РїРµСЂРІРѕРіРѕ СЂРµР·СѓР»СЊС‚Р°С‚Р°: '{first_result}'")

    with allure.step("РџСЂРѕРІРµСЂРєР°: РІ РїРµСЂРІРѕРј СЂРµР·СѓР»СЊС‚Р°С‚Рµ РїРѕРёСЃРєР° РїСЂРёСЃСѓС‚СЃС‚РІСѓРµС‚ 'Python'"):
        assert "python" in first_result.lower(), f"РћР¶РёРґР°Р»Р°СЃСЊ РїРѕРґСЃС‚СЂРѕРєР° 'Python', РЅРѕ РїРѕР»СѓС‡РёР»Рё: '{first_result}'"
