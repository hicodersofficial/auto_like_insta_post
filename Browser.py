from selenium import webdriver
from colorama import Fore
from Display import Display

class Browser(Display):
    def __init__(self, args):
        self.driver = None
        if len(args) > 2:
            if '-b' in args:
                self.driver = args[args.index('-b')+1]
            if '--browser' in args:
                self.driver = args[args.index('--browser')+1]

        if self.driver != None:
            if self.driver.lower() == "chrome":
                super().chosen_browser('chrome')
                self.browser = webdriver.Chrome()
            if self.driver.lower() == "opera":
                super().chosen_browser('opera')
                self.browser = webdriver.Opera()
            if self.driver.lower() == "firefox":
                super().chosen_browser('firefox')
                self.browser = webdriver.Firefox()
            if self.driver.lower() == "safari":
                super().chosen_browser('safari')
                self.browser = webdriver.Safari()
            if self.driver.lower() == "ie":
                super().chosen_browser('ie')
                self.browser = webdriver.Ie()
        else:
            super().chosen_browser('chrome')
            self.browser = webdriver.Chrome()