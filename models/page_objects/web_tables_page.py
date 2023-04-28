from typing import List

from selenium.webdriver.common.by import By

from models.page_objects.base_demoqa_page import BaseDemoqaPage
from models.regisration_form import RegistrationForm
from models.user import User
from webdriver.wait_utils import WaitUtils


class WebTablesPage(BaseDemoqaPage):
    def __init__(self):
        unique_element_locator = (By.CLASS_NAME, "main-header")
        header_text = "Web Tables"
        super().__init__(unique_element_locator, header_text)
        self.__add_button_locator = (By.ID, "addNewRecordButton")
        self.__all_filled_rows_locator = (By.XPATH, "//div[@class='rt-tr-group' and "
                                                    "./div/div[string-length(text())>0]]")
        self.__each_cell_in_row_locator = (By.XPATH, ".//div[@class='rt-td']")
        self.__edit_button_locator = (By.XPATH, ".//span[@title='Edit']/*")
        self.__delete_button_locator = (By.XPATH, ".//span[@title='Delete']/*")

    def click_the_add_button(self):
        WaitUtils.wait_and_click_an_element(self.__add_button_locator)

    def add_user_to_the_table(self, user: User):
        self.click_the_add_button()
        registration_form = RegistrationForm()
        registration_form.fill_fields_with_data(user)
        registration_form.click_the_submit_button()

    def is_the_user_in_the_table(self, user) -> bool:
        return user in self.get_all_users_from_the_table()

    def get_all_users_from_the_table(self) -> List[User]:
        list_of_filled_rows = WaitUtils.wait_and_find_elements(self.__all_filled_rows_locator)
        list_of_table_users = []
        for row in list_of_filled_rows:
            user_data = row.text.split("\n")
            user = User.new_user_from_list_of_strings(user_data)
            list_of_table_users.append(user)
        return list_of_table_users

    def click_edit_button_of_user_number(self, user_number: int):
        user_row = WaitUtils.wait_and_find_elements(self.__all_filled_rows_locator)[user_number - 1]
        user_row.find_element(*self.__edit_button_locator).click()

    def edit_user_fields(self, number_of_user_to_edit: int, user_with_data_for_replacing: User):
        self.click_edit_button_of_user_number(number_of_user_to_edit)
        registration_form = RegistrationForm()
        registration_form.replace_fields_with_data_of_user(user_with_data_for_replacing)
        registration_form.click_the_submit_button()

    def get_user_from_row_number(self, row_number: int):
        return self.get_all_users_from_the_table()[row_number - 1]

    def delete_user_number(self, user_number: int):
        user_row = WaitUtils.wait_and_find_elements(self.__all_filled_rows_locator)[user_number - 1]
        user_row.find_element(*self.__delete_button_locator).click()


