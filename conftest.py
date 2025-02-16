import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LogInPageLocators, MainPageLocators
from data import LOGIN_URL, MAIN_URL, REGISTER_USER


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture()
def user_main_page_driver(driver):
    driver.get(LOGIN_URL)

    driver.find_element(By.XPATH, LogInPageLocators.EMAIL_INPUT).send_keys(REGISTER_USER['login'])
    driver.find_element(By.XPATH, LogInPageLocators.PASSWORD_INPUT).send_keys(REGISTER_USER['password'])

    WebDriverWait(driver, 3)
    driver.find_element(By.XPATH, LogInPageLocators.ENTER_BTN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.url_changes(LOGIN_URL)
    )


@pytest.fixture()
def user_account_page_driver(driver, user_main_page_driver):
    WebDriverWait(driver, 3)
    driver.find_element(By.XPATH, MainPageLocators.ACCOUNT_A).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.url_changes(MAIN_URL)
    )
