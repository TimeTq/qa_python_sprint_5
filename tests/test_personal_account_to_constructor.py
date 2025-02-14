import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountPageLocators, MAIN_URL


CONSTRUCTOR_PARAMS = [
    # * Переход по клику на логотип Stellar Burgers.
    AccountPageLocators.MAIN_LOGO_A,
    # * Переход по клику на «Конструктор»
    AccountPageLocators.CONSTRUCTOR_A,
]


@pytest.mark.parametrize('tested_button_x_path', CONSTRUCTOR_PARAMS)
def test_user_click_button_account_page_login_account_main_page(
        tested_button_x_path: str,
        register_user: dict[str, str],
        user_account_page_driver: WebDriver,
) -> None:
    try:
        WebDriverWait(user_account_page_driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tested_button_x_path))
        )

        user_account_page_driver.find_element(By.XPATH, tested_button_x_path).click()
        assert user_account_page_driver.current_url == MAIN_URL

    finally:
        user_account_page_driver.quit()


