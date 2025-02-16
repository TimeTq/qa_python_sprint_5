import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators, LogInPageLocators, RegisterPageLocators, RecoveryPasswordPageLocators
from data import REGISTRATION_URL, RECOVERY_PASSWORD_URL, MAIN_URL, LOGIN_URL, REGISTER_USER

LOGIN_TEST_PARAMS = [
    # * вход по кнопке «Войти в аккаунт» на главной
    (MAIN_URL, MainPageLocators.LOGIN_BTN),
    # * вход через кнопку «Личный кабинет»
    (MAIN_URL, MainPageLocators.ACCOUNT_A),
    # * вход через кнопку в форме регистрации
    (REGISTRATION_URL, RegisterPageLocators.LOGIN_A),
    # * вход через кнопку в форме восстановления пароля
    (RECOVERY_PASSWORD_URL, RecoveryPasswordPageLocators.LOGIN_A),
]


class TestLogIn:
    @staticmethod
    @pytest.mark.parametrize('start_page, login_redirect_locator', LOGIN_TEST_PARAMS)
    def test_user_enter_from_pages_user_cred_main_page(
            start_page: str,
            login_redirect_locator: str,
            driver: WebDriver,
    ) -> None:
        driver.get(start_page)

        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, login_redirect_locator).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LogInPageLocators.EMAIL_INPUT))
        )
        driver.find_element(By.XPATH, LogInPageLocators.EMAIL_INPUT).send_keys(REGISTER_USER['login'])
        driver.find_element(By.XPATH, LogInPageLocators.PASSWORD_INPUT).send_keys(REGISTER_USER['password'])

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, LogInPageLocators.ENTER_BTN))
        )
        driver.find_element(By.XPATH, LogInPageLocators.ENTER_BTN).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_changes(LOGIN_URL))
        assert driver.current_url == MAIN_URL
