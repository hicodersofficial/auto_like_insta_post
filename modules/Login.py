from getpass import getpass
from modules.Display import Display
from time import sleep
from selenium.webdriver.common.keys import Keys  
from config.global_variables import URL
from config.scripts import USERNAMETEXTBOX_X_PATH, PASSWORDTEXTBOX_X_PATH, SUBMITBUTTON_CSS_SELECTOR

class Login(Display):
    def __init__(self):
        self.username = input("Enter your username: ").lower()
        self.password = getpass("Enter instagram password: ")

        if self.password == "" or self.username == "":
            super().warning("Password and username both fields are required.")
            self.__init__()

    def login(self, browser, internetTime):
        super().navigating_url(URL)
        browser.get(URL)

        super().wait_time(internetTime)
        sleep(internetTime)

        browser.find_element_by_xpath(USERNAMETEXTBOX_X_PATH).send_keys(self.username + Keys.TAB)
        browser.find_element_by_xpath(PASSWORDTEXTBOX_X_PATH).send_keys(self.password)
        browser.execute_script(SUBMITBUTTON_CSS_SELECTOR)

        super().account(self.username)
        super().wait_time(internetTime * 1.5)
        sleep(internetTime * 1.5)

