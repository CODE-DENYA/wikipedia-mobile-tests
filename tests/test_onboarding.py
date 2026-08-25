import allure
from pages.onboarding_page import OnboardingPage


def test_onboarding_flow(driver):
    """РџСЂРѕРІРµСЂРєР° РґРёРЅР°РјРёС‡РµСЃРєРѕРіРѕ РїСЂРѕС…РѕР¶РґРµРЅРёСЏ РѕРЅР±РѕСЂРґРёРЅРіР°."""
    onboarding = OnboardingPage(driver)

    with allure.step("РџСЂРѕРІРµСЂРєР° РѕС‚РѕР±СЂР°Р¶РµРЅРёСЏ РїРµСЂРІРѕРіРѕ СЌРєСЂР°РЅР°"):
        assert (
            onboarding.is_primary_text_displayed()
        ), "РџРµСЂРІС‹Р№ СЌРєСЂР°РЅ РѕРЅР±РѕСЂРґРёРЅРіР° РЅРµ РѕС‚РѕР±СЂР°Р¶Р°РµС‚СЃСЏ"

    onboarding.complete_onboarding()
