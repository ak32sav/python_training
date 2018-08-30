

class ContactHelper:

    def __init__(self, app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        # open contact creation page
        wd.find_element_by_link_text("add new").click()
        # fill the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.fname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_homepage()

    def edit_first_contact(self):
        wd = self.app.wd
        self.app.open_homepage()
        # select first contact and click on Edit
        wd.find_element_by_xpath("//a/img[@title='Edit']").click()
        # edit values of the fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(" edited")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(" edited")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(" edited")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(" edited")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(" edited")
        # submit
        wd.find_element_by_xpath("//input[@name='update' and @value='Update']").click()
        self.app.open_homepage()

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