from selenium.webdriver.common.by import By

from models.page_objects.base_demoqa_page import BaseDemoqaPage
from webdriver.wait_utils import WaitUtils


class AutomationPracticePage(BaseDemoqaPage):

    def __init__(self):
        unique_element_locator = (By.CLASS_NAME, 'main-header')
        header_text = "Practice Form"
        super().__init__(unique_element_locator, header_text)

        self.__body_locator = (By.TAG_NAME, 'body')
        self.__header_locator = (By.TAG_NAME, 'header')
        self.__footer_locator = (By.TAG_NAME, 'footer')
        self.__side_menu_locator = (By.CLASS_NAME, 'left-pannel')
        self.__first_name_locator = (By.ID, "firstName")
        self.__last_name_locator = (By.ID, "lastName")
        self.__user_email_locator = (By.ID, "userEmail")
        self.__male_radio_locator = (By.XPATH, "//label[contains(text(),'Male')]")
        self.__female_radio_locator = (By.XPATH, "//label[contains(text(),'Female')]")
        self.__other_radio_locator = (By.XPATH, "//label[contains(text(),'Other')]")
        self.__mobile_field_locator = (By.ID, "userNumber")
        self.__date_of_birth_field_locator = (By.ID, "dateOfBirthInput")
        self.__subjects_field_locator = (By.ID, "subjectsInput")
        self.__sports_checkbox_field_locator = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
        self.__reading_checkbox_field_locator = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
        self.__music_checkbox_field_locator = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
        self.__upload_picture_button_locator = (By.ID, "uploadPicture")
        self.__current_address_field_locator = (By.ID, "currentAddress")
        self.__select_state_dropdown_locator = (By.XPATH, "//div[contains(text(),'Select State')]")
        self.__select_city_dropdown_locator = (By.XPATH, "//div[contains(text(),'Select City')]")
        self.__submit_button_locator = (By.ID, "submit")

    def first_name_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__first_name_locator).is_displayed()

    def last_name_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__last_name_locator).is_displayed()

    def user_email_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__user_email_locator).is_displayed()

    def male_radio_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__male_radio_locator).is_displayed()

    def female_radio_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__female_radio_locator).is_displayed()

    def other_radio_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__other_radio_locator).is_displayed()

    def mobile_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__mobile_field_locator).is_displayed()

    def date_of_birth_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__date_of_birth_field_locator).is_displayed()

    def subjects_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__subjects_field_locator).is_displayed()

    def sports_checkbox_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__sports_checkbox_field_locator).is_displayed()

    def reading_checkbox_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__reading_checkbox_field_locator).is_displayed()

    def music_checkbox_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__music_checkbox_field_locator).is_displayed()

    def upload_picture_button_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__upload_picture_button_locator).is_displayed()

    def current_address_field_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__current_address_field_locator).is_displayed()

    def select_state_dropdown_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__select_state_dropdown_locator).is_displayed()

    def select_city_dropdown_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__select_city_dropdown_locator).is_displayed()

    def submit_button_is_visible(self) -> bool:
        return WaitUtils.wait_and_find_an_element(self.__submit_button_locator).is_displayed()

    def header_is_visible(self):
        return WaitUtils.wait_and_find_an_element(self.__header_locator).is_displayed()

    def footer_is_visible(self):
        return WaitUtils.wait_and_find_an_element(self.__footer_locator).is_displayed()

    def side_menu_is_visible(self):
        return WaitUtils.wait_and_find_an_element(self.__side_menu_locator).is_displayed()

    def get_source_text(self):
        return WaitUtils.wait_and_find_an_element(self.__body_locator).text
