from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        #self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/index.php" and len(wd.find_elements_by_name("new")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

