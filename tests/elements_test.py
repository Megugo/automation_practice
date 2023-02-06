import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            #input_data = text_box_page.fill_all_fields()
            out_full_name, out_email, out_cur_address, out_perm_address = text_box_page.check_fields_form()
            #output_data = text_box_page.check_fields_form()

            assert full_name == out_full_name, "full name is not matched"
            assert email == out_email, "email is not matched"
            assert current_address == out_cur_address, "current address is not matched"
            assert permanent_address == out_perm_address, "permanent address is not matched"
            #assert input_data == output_data

    class TestCheckBox:

        def test_check_box(self, driver):

            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()

            assert input_checkboxes == output_result, "Input checkboxes not mathced with results"






