from webdriver.wait_utils import WaitUtils


class BaseDemoqaPage:

    def __init__(self, unique_element_locator, header_text):
        self.__unique_element_locator = unique_element_locator
        self.__header_text = header_text

    def is_visible(self) -> bool:
        header = WaitUtils.wait_and_find_an_element(self.__unique_element_locator)
        return header.is_displayed() and header.text == self.__header_text
