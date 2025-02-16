from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountPageLocators
from data import LOGIN_URL, ACCOUNT_URL


class TestLogOut:
    @staticmethod
    def test_user_exit_from_account_page_login_account_login_page(driver: WebDriver, user_account_page_driver) -> None:
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, AccountPageLocators.LOGOUT_BTN))
        )
        driver.find_element(By.XPATH, AccountPageLocators.LOGOUT_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_changes(ACCOUNT_URL)
        )
        assert driver.current_url == LOGIN_URL
