import allure

from models.automation_practice_page import AutomationPracticePage
from test_base_web import TestBaseWeb


@allure.title("Test of the automation practice form on demoqa.com")
class TestSmokeDemoqa(TestBaseWeb):

    @allure.description("Check the presence of all key elements on the 'automation practice' page")
    def test_all_key_elements_present_on_automation_practice_page(self):
        automation_practice_page = AutomationPracticePage()

        assert automation_practice_page.is_visible(), "This is not Practice Form page"

        assert automation_practice_page.header_is_visible(), "There's no header on page"
        assert automation_practice_page.footer_is_visible(), "There's no footer on page"
        assert automation_practice_page.side_menu_is_visible(), "There's no side menu on page"

        key_labels = self.config["test_data"]["key_labels"].split(', ')
        for label in key_labels:
            assert label in automation_practice_page.get_source_text(), f"There's no '{label}' label on page"

        assert automation_practice_page.first_name_field_is_visible(), "There's no first name field on page"
        assert automation_practice_page.last_name_field_is_visible(), "There's no last name field on page"
        assert automation_practice_page.user_email_field_is_visible(), "There's no user email field on page"
        assert automation_practice_page.male_radio_is_visible(), "There's no male radio checkbox on page"
        assert automation_practice_page.female_radio_is_visible(), "There's no female radio checkbox on page"
        assert automation_practice_page.other_radio_is_visible(), "There's no 'other' radio checkbox on page"
        assert automation_practice_page.mobile_field_is_visible(), "There's no mobile field on page"
        assert automation_practice_page.date_of_birth_field_is_visible(), "There's no date of birth field on page"
        assert automation_practice_page.subjects_field_is_visible(), "There's no subjects field on page"
        assert automation_practice_page.sports_checkbox_is_visible(), "There's no sports checkbox on page"
        assert automation_practice_page.reading_checkbox_is_visible(), "There's no reading checkbox on page"
        assert automation_practice_page.music_checkbox_is_visible(), "There's no music checkbox on page"
        assert automation_practice_page.upload_picture_button_is_visible(), "There's no upload picture button on page"
        assert automation_practice_page.current_address_field_is_visible(), "There's no current address field on page"
        assert automation_practice_page.select_state_dropdown_is_visible(), "There's no select state dropdown on page"
        assert automation_practice_page.select_city_dropdown_is_visible(), "There's no select city dropdown on page"
        assert automation_practice_page.submit_button_is_visible(), "There's no submit button on page"
