from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.helpers import Helpers


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.helper = Helpers(self)


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

