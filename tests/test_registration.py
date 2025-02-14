from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import RegisterPageLocators, REGISTRATION_URL, LOGIN_URL


def do_register(
        driver: WebDriver,
        user_name: str,
        user_login: str,
        user_password: str,
) -> None:
    driver.find_element(By.XPATH, RegisterPageLocators.NAME_INPUT).send_keys(user_name)
    driver.find_element(By.XPATH, RegisterPageLocators.EMAIL_INPUT).send_keys(user_login)
    driver.find_element(By.XPATH, RegisterPageLocators.PASSWORD_INPUT).send_keys(user_password)

    WebDriverWait(driver, 1).until(
        expected_conditions.element_to_be_clickable((By.XPATH, RegisterPageLocators.REGISTRATION_BTN))
    )

    driver.find_element(By.XPATH, RegisterPageLocators.REGISTRATION_BTN).click()


def test_user_registration_allowed_credentials_success_registration(
        user_name: str,
        user_login: str,
        user_password: str,
        driver: WebDriver
) -> None:
    driver.get(REGISTRATION_URL)
    do_register(driver, user_name, user_login, user_password)

    WebDriverWait(driver, 3).until(
        expected_conditions.url_changes(REGISTRATION_URL)
    )

    assert driver.current_url == LOGIN_URL
    driver.quit()


def test_user_registration_short_password_bad_password_warning(
        user_name: str,
        user_password: str,
        driver: WebDriver
) -> None:
    driver.get(REGISTRATION_URL)
    do_register(driver, user_name, f'{user_name}@qwerty.ru', user_password[:3])

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterPageLocators.ENTER_CREDENTIALS_FORM))
    )

    assert driver.find_elements(By.XPATH, RegisterPageLocators.ERROR_PASSWORD_P)
    driver.quit()
