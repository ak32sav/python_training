from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        # open contact creation page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_homepage()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(new_contact_data, index)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_homepage()
        # select first contact and click on Edit
        wd.find_elements_by_xpath("//a/img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@name='update' and @value='Update']").click()
        self.app.open_homepage()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("email", contact.email)
        self.change_field_value("home", contact.home_phone)

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        # select and click on Delete button
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept deleting
        wd.switch_to_alert().accept()
        self.app.open_homepage()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                fname = element.find_element_by_xpath(".//td[3]").text
                lname = element.find_element_by_xpath(".//td[2]").text
                id=element.find_element_by_xpath(".//input").get_attribute("value")
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(fname=fname, lname=lname, id=id,
                                                  all_phones_from_homepage=all_phones
                                                  ))
        return list(self.contact_cache)

    def open_edit_contact_form_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_xpath("//a/img[@title='Edit']")[index].click()


    def open_view_contact_form_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_xpath("//a/img[@title='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_contact_form_by_index(index)
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        fname = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(fname=fname, lname=lname, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone
                       )

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_form_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)
