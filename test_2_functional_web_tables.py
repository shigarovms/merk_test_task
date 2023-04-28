import allure

from models.user import User
from models.web_tables_page import WebTablesPage
from test_base_web import TestBaseWeb


@allure.title("Test of the functionality of web tables on demoqa.com")
class TestFuncWebTables(TestBaseWeb):

    @allure.description("Test if new record can be added to the table")
    def test_of_a_new_record_creation(self):
        web_tables_page = WebTablesPage()
        assert web_tables_page.is_visible(), "This is not Web Tables page"

        user_to_add = User.new_user_from_json(self.config["test_data"]["new_user_json_path"])
        web_tables_page.add_user_to_the_table(user_to_add)
        assert web_tables_page.is_the_user_in_the_table(user_to_add)

    @allure.description("Test of editing a record in the table")
    def test_of_editing_a_record(self):
        web_tables_page = WebTablesPage()
        assert web_tables_page.is_visible(), "This is not Web Tables page"

        user_with_new_data = User.new_user_from_json(self.config["test_data"]["new_user_json_path"])
        number_of_user_to_edit = int(self.config["test_data"]["num_of_record_to_edit"])
        user_with_old_data = web_tables_page.get_user_from_row_number(number_of_user_to_edit)
        assert not web_tables_page.is_the_user_in_the_table(user_with_new_data), \
            "User with same data is already in the table"
        web_tables_page.edit_user_fields(number_of_user_to_edit, user_with_new_data)
        assert web_tables_page.is_the_user_in_the_table(user_with_new_data), "There's no user with new data"
        assert not web_tables_page.is_the_user_in_the_table(user_with_old_data), \
            "The old user's data is still in the table"

    @allure.description("Test of deleting a record from the table")
    def test_of_deleting_a_record(self):
        web_tables_page = WebTablesPage()
        assert web_tables_page.is_visible(), "This is not Web Tables page"

        number_of_user_to_delete = int(self.config["test_data"]["num_of_record_to_delete"])
        user_to_delete = web_tables_page.get_user_from_row_number(number_of_user_to_delete)
        web_tables_page.delete_user_number(number_of_user_to_delete)
        assert not web_tables_page.is_the_user_in_the_table(user_to_delete), "The old user's data is still in the table"
