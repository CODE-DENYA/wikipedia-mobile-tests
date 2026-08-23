from appium.webdriver.common.appiumby import AppiumBy


def test_onboarding_screen_is_displayed(driver):
    """Проверка загрузки первого экрана онбординга."""

    # Поиск заголовка / текста на первом экране
    primary_text = driver.find_element(
        AppiumBy.XPATH,
        "//*[contains(@text, 'All the world') or contains(@text, 'Free encyclopedia') or contains(@text, 'Wikipedia')]",
    )

    assert primary_text.is_displayed(), (
        "Заголовок онбординга должен отображаться"
    )