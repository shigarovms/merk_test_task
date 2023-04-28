from webdriver.browser_factory import BrowserFactory


class WebDriver:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = BrowserFactory.create_browser()
        return cls._instance

    @classmethod
    def teardown(cls):
        cls._instance = None
