from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import RegisterPageLocators
from data import REGISTRATION_URL, LOGIN_URL
from helpers import get_user_name, get_user_login, get_user_password


class TestRegistration:
    @staticmethod
    def test_user_registration_allowed_credentials_success_registration(driver: WebDriver) -> None:
        driver.get(REGISTRATION_URL)

        driver.find_element(By.XPATH, RegisterPageLocators.NAME_INPUT).send_keys(get_user_name())
        driver.find_element(By.XPATH, RegisterPageLocators.EMAIL_INPUT).send_keys(get_user_login())
        driver.find_element(By.XPATH, RegisterPageLocators.PASSWORD_INPUT).send_keys(get_user_password())

        WebDriverWait(driver, 1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, RegisterPageLocators.REGISTRATION_BTN))
        )

        driver.find_element(By.XPATH, RegisterPageLocators.REGISTRATION_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_changes(REGISTRATION_URL)
        )

        assert driver.current_url == LOGIN_URL


    @staticmethod
    def test_user_registration_short_password_bad_password_warning(driver: WebDriver) -> None:
        driver.get(REGISTRATION_URL)

        driver.find_element(By.XPATH, RegisterPageLocators.NAME_INPUT).send_keys(get_user_name())
        driver.find_element(By.XPATH, RegisterPageLocators.EMAIL_INPUT).send_keys(get_user_login())
        driver.find_element(By.XPATH, RegisterPageLocators.PASSWORD_INPUT).send_keys(get_user_password()[:3])

        WebDriverWait(driver, 1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, RegisterPageLocators.REGISTRATION_BTN))
        )

        driver.find_element(By.XPATH, RegisterPageLocators.REGISTRATION_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, RegisterPageLocators.ENTER_CREDENTIALS_FORM))
        )

        assert driver.find_elements(By.XPATH, RegisterPageLocators.ERROR_PASSWORD_P)
