from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_USER
from locators import AccountPageLocators


class TestPersonalAccount:
    @staticmethod
    def test_user_exit_from_account_page_login_account_login_page(
            driver: WebDriver,
            user_account_page_driver,
    ) -> None:
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AccountPageLocators.USER_NAME_INPUT))
        )

        page_name = driver.find_element(By.XPATH, AccountPageLocators.USER_NAME_INPUT)\
            .get_attribute('value')
        page_login = driver.find_element(By.XPATH, AccountPageLocators.USER_LOGIN_INPUT)\
            .get_attribute('value')

        assert page_name == REGISTER_USER['name'] \
               and page_login == REGISTER_USER['login'].lower()  # ? почему почта выводится в нижнем регистре
