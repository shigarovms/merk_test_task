from selenium.webdriver.common.by import By

from models.user import User
from webdriver.wait_utils import WaitUtils


class RegistrationForm:
    def __init__(self):
        self.__first_name_field = WaitUtils.wait_and_find_an_element((By.ID, "firstName"))
        self.__last_name_field = WaitUtils.wait_and_find_an_element((By.ID, "lastName"))
        self.__email_field = WaitUtils.wait_and_find_an_element((By.ID, "userEmail"))
        self.__age_field = WaitUtils.wait_and_find_an_element((By.ID, "age"))
        self.__salary_field = WaitUtils.wait_and_find_an_element((By.ID, "salary"))
        self.__department_field = WaitUtils.wait_and_find_an_element((By.ID, "department"))
        self.__submit_button = WaitUtils.wait_and_find_an_element((By.ID, "submit"))

    def fill_fields_with_data(self, user: User):
        self.__first_name_field.clear()
        self.__first_name_field.send_keys(user.first_name)
        self.__last_name_field.clear()
        self.__last_name_field.send_keys(user.last_name)
        self.__email_field.clear()
        self.__email_field.send_keys(user.email)
        self.__age_field.clear()
        self.__age_field.send_keys(user.age)
        self.__salary_field.clear()
        self.__salary_field.send_keys(user.salary)
        self.__department_field.clear()
        self.__department_field.send_keys(user.department)

    def click_the_submit_button(self):
        self.__submit_button.click()

    def replace_fields_with_data_of_user(self, user: User):
        self.clear_all_fields()
        self.fill_fields_with_data(user)

    def clear_all_fields(self):
        self.__first_name_field.clear()
        self.__last_name_field.clear()
        self.__email_field.clear()
        self.__age_field.clear()
        self.__salary_field.clear()
        self.__department_field.clear()



