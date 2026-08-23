from pages.onboarding_page import OnboardingPage


def test_onboarding_flow(driver):
    """Проверка динамического прохождения онбординга."""
    onboarding = OnboardingPage(driver)

    assert (
        onboarding.is_primary_text_displayed()
    ), "Первый экран онбординга не отображается"

    # Проходим все шаги независимо от их точного количества
    onboarding.complete_onboarding()