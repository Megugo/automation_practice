import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_fields_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPEND_ALL).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            item_title = box.find_element("xpath", self.locators.ITEM_TITLE)
            data.append(item_title.text)

        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)

        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_random_RB(self):
        item_list = self.elements_are_visible(self.locators.ALL_ACTIVE_RADIO_BUTTONS)
        count = 3
        while count != 0:
            item = item_list[random.randint(0, 1)]
            item.click()
            item_text = item.text
            count -= 1
        return item_text

    def click_radio_button(self, choice):
        choices = {'yes': self.locators.YES,
                   'impressive': self.locators.IMPRESSIVE,
                   'no': self.locators.NO}
        self.element_is_visible(choices[choice]).click()

    def get_RB_result(self):
        result = self.element_is_present(self.locators.RESULT)

        return result.text

class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()

            count-=1
        return [firstname, lastname, str(age), email,  str(salary), department]

    def check_new_person(self):
        persons_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        data = []
        for item in persons_list:
            data.append(item.text.splitlines())

        return data

    def search_person(self,key):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return age

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_delete(self):
        return self.element_is_present(self.locators.NP_ROWS).text

    def change_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []

        for i in count:
            count_rows_button = self.element_is_visible(self.locators.COUNT_ROWS)
            self.go_to_element(count_rows_button)
            count_rows_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{i}"]')).click
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)





