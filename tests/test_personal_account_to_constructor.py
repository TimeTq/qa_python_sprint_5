import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountPageLocators
from data import MAIN_URL


CONSTRUCTOR_PARAMS = [
    # * Переход по клику на логотип Stellar Burgers.
    AccountPageLocators.MAIN_LOGO_A,
    # * Переход по клику на «Конструктор»
    AccountPageLocators.CONSTRUCTOR_A,
]


class TestPersonalAccountToConstructor:
    @staticmethod
    @pytest.mark.parametrize('tested_button_x_path', CONSTRUCTOR_PARAMS)
    def test_user_click_button_account_page_login_account_main_page(
            driver: WebDriver,
            tested_button_x_path: str,
            user_account_page_driver,
    ) -> None:
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, tested_button_x_path))
        )

        driver.find_element(By.XPATH, tested_button_x_path).click()
        assert driver.current_url == MAIN_URL
