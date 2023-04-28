from configparser import ConfigParser
from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from webdriver.singleton_webdriver import WebDriver


class WaitUtils:
    __config = ConfigParser()
    __config.read('config.ini')
    __timeout = int(__config['main']['wait_timeout'])
    __poll_frequency = float(__config['main']['poll_frequency'])

    @classmethod
    def wait_and_find_an_element(cls, locator) -> WebElement:
        return WebDriverWait(WebDriver(), timeout=cls.__timeout, poll_frequency=cls.__poll_frequency)\
                                    .until(ec.presence_of_element_located(locator))

    @classmethod
    def wait_and_click_an_element(cls, locator):
        return WebDriverWait(WebDriver(), timeout=cls.__timeout, poll_frequency=cls.__poll_frequency)\
                                    .until(ec.element_to_be_clickable(locator)).click()

    @classmethod
    def wait_and_find_elements(cls, locator) -> List[WebElement]:
        return WebDriverWait(WebDriver(), timeout=cls.__timeout, poll_frequency=cls.__poll_frequency)\
                                    .until(ec.presence_of_all_elements_located(locator))
