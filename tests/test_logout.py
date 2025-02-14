from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LOGIN_URL, ACCOUNT_URL, AccountPageLocators


def test_user_exit_from_account_page_login_account_login_page(user_account_page_driver: WebDriver) -> None:
    try:
        WebDriverWait(user_account_page_driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, AccountPageLocators.LOGOUT_BTN))
        )
        user_account_page_driver.find_element(By.XPATH, AccountPageLocators.LOGOUT_BTN).click()

        WebDriverWait(user_account_page_driver, 3).until(
            expected_conditions.url_changes(ACCOUNT_URL)
        )
        assert user_account_page_driver.current_url == LOGIN_URL

    finally:
        user_account_page_driver.quit()
