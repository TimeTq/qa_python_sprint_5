import random
from string import ascii_lowercase, ascii_uppercase, digits

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LOGIN_URL, MAIN_URL, LogInPageLocators, MainPageLocators

ALPHABET = ascii_uppercase + ascii_lowercase + digits
LENGTH = 8


@pytest.fixture(scope='session')
def user_name():
    return ''.join(random.choices(ALPHABET, k=LENGTH))


@pytest.fixture(scope='session')
def user_login():
    login = ''.join(random.choices(ALPHABET, k=LENGTH))
    domain = 'ya'
    return f'{login}@{domain}.ru'


@pytest.fixture(scope='session')
def user_password():
    return ''.join(random.choices(ALPHABET, k=LENGTH))


@pytest.fixture(scope='session')
def register_user():
    return {
        'name': '8PhWGOJt',
        'login': '4O21Unjy@ya.ru',
        'password': 'nQXAEODH',
    }


@pytest.fixture()
def driver():
    service = webdriver.ChromeService(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    return driver


@pytest.fixture()
def user_main_page_driver(driver, register_user):
    driver.get(LOGIN_URL)

    driver.find_element(By.XPATH, LogInPageLocators.EMAIL_INPUT).send_keys(register_user['login'])
    driver.find_element(By.XPATH, LogInPageLocators.PASSWORD_INPUT).send_keys(register_user['password'])

    WebDriverWait(driver, 3)
    driver.find_element(By.XPATH, LogInPageLocators.ENTER_BTN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.url_changes(LOGIN_URL)
    )

    return driver


@pytest.fixture()
def user_account_page_driver(user_main_page_driver, register_user):
    WebDriverWait(user_main_page_driver, 3)
    user_main_page_driver.find_element(By.XPATH, MainPageLocators.ACCOUNT_A).click()

    WebDriverWait(user_main_page_driver, 3).until(
        expected_conditions.url_changes(MAIN_URL)
    )
    return user_main_page_driver
