import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            #input_data = text_box_page.fill_all_fields()
            out_full_name, out_email, out_cur_address, out_perm_address = text_box_page.check_fields_form()
            #output_data = text_box_page.check_fields_form()
            time.sleep(2)
            assert full_name == out_full_name, "full name is not matched"
            assert email == out_email, "email is not matched"
            assert current_address == out_cur_address, "current address is not matched"
            assert permanent_address == out_perm_address, "permanent address is not matched"
            #assert input_data == output_data

