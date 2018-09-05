from model.contact import Contact

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

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_homepage()
        # select first contact and click on Edit
        wd.find_element_by_xpath("//a/img[@title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit
        wd.find_element_by_xpath("//input[@name='update' and @value='Update']").click()
        self.app.open_homepage()

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
        wd = self.app.wd
        self.app.open_homepage()
        # select and click on Delete button
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept deleting
        wd.switch_to_alert().accept()
        self.app.open_homepage()

    def count(self):
        wd = self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.open_homepage()
        contacts_list = []
        name=None
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            fname = element.find_element_by_xpath(".//td[3]").text
            lname = element.find_element_by_xpath(".//td[2]").text
            id=element.find_element_by_xpath(".//input").get_attribute("value")
            contacts_list.append(Contact(fname=fname, lname=lname, id=id))
        return contacts_list

