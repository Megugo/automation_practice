import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


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

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            #input_radio_button = radio_button_page.click_random_RB()
            radio_button_page.click_radio_button('yes')
            output_RB_yes = radio_button_page.get_RB_result()
            radio_button_page.click_radio_button('impressive')
            output_RB_impressive = radio_button_page.get_RB_result()
            radio_button_page.click_radio_button('no')
            output_RB_no = radio_button_page.get_RB_result()

            assert output_RB_yes == "Yes", "'Yes' haven't been selected"
            assert output_RB_impressive == "Impressive", "'Impressive' haven't been selected"
            assert output_RB_no == "No", "'No' haven't been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            input_data = web_table_page.add_new_person()
            output_data = web_table_page.check_new_person()

            assert input_data in output_data, "Person added incorrectly"  #падает при длинном названии профессии

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person wasn't found in table"

        def test_web_table_update_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            firstname = web_table_page.add_new_person()[0]
            web_table_page.search_person(firstname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person info wasn't change"

        def test_web_table_delet_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.delete_person(email)
            text = web_table_page.check_delete()
            assert text in "No rows found", "the person info wasn't deleted"

        def test_web_table_change_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.change_rows()
            assert [5, 10, 20, 25, 50, 100] == count, "Numbers of rows in the table changed incorrectly"












