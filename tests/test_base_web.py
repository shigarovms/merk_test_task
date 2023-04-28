from configparser import ConfigParser

import pytest

from webdriver.singleton_webdriver import WebDriver


class TestBaseWeb:
    config = ConfigParser()
    config.read("config.ini")

    @pytest.fixture(autouse=True)
    def setup(self):
        url = self.config["urls"][self.__class__.__name__]
        driver = WebDriver()
        driver.get(url)
        yield
        driver.quit()
        WebDriver.teardown()
