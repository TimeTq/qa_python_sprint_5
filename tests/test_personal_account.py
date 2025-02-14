from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountPageLocators


def test_user_exit_from_account_page_login_account_login_page(
        register_user: dict[str, str],
        user_account_page_driver: WebDriver,
) -> None:
    try:
        WebDriverWait(user_account_page_driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AccountPageLocators.USER_NAME_INPUT))
        )

        page_name = user_account_page_driver.find_element(By.XPATH, AccountPageLocators.USER_NAME_INPUT)\
            .get_attribute('value')
        page_login = user_account_page_driver.find_element(By.XPATH, AccountPageLocators.USER_LOGIN_INPUT)\
            .get_attribute('value')

        assert page_name == register_user['name'] \
               and page_login == register_user['login'].lower()  # ? почему почта выводится в нижнем регистре

    finally:
        user_account_page_driver.quit()
