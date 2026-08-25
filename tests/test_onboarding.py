import allure
from pages.onboarding_page import OnboardingPage


@allure.epic("Онбординг")
@allure.title("Проверка динамического прохождения онбординга")
def test_onboarding_flow(driver):
    """Проверка динамического прохождения онбординга."""
    onboarding = OnboardingPage(driver)

    with allure.step("Проверка отображения первого экрана"):
        assert (
            onboarding.is_primary_text_displayed()
        ), "Первый экран онбординга не отображается"

    onboarding.complete_onboarding()