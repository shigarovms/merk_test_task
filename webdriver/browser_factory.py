from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    @staticmethod
    def create_browser() -> webdriver:
        _config = ConfigParser()
        _config.read('config.ini')
        _browser_name = _config['main']['browser'].lower()
        _arguments = _config['browser_options'][_browser_name].split(', ')

        if _browser_name == "chrome":
            options = webdriver.ChromeOptions()
            for argument in _arguments:
                options.add_argument(argument)
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif _browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            for argument in _arguments:
                options.add_argument(argument)
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: {_browser_name}")