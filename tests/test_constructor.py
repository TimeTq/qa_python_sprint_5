import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MAIN_URL, MainPageLocators


CONSTRUCTOR_TEST_PARAMS = [
    # * переходы к «Булки»
    MainPageLocators.BUN_DIV,
    # * переходы к «Соусы»
    MainPageLocators.SAUCE_DIV,
    # * переходы к «Начинки»
    MainPageLocators.FILLING_DIV,
]


@pytest.mark.parametrize('constructor_x_path', CONSTRUCTOR_TEST_PARAMS)
def test_click_on_constructor_x_path_class_added_to_element(constructor_x_path: str, driver: WebDriver) -> None:
    try:
        driver.get(MAIN_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, constructor_x_path))
        )

        div = driver.find_element(By.XPATH, constructor_x_path)
        driver.execute_script("arguments[0].click();", div)

        assert 'tab_tab_type_current__2BEPc' in div.get_attribute('class')

    finally:
        driver.quit()
