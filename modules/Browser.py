from selenium import webdriver
from colorama import Fore
from modules.Display import Display
import sys

class Browser(Display):
    def __init__(self, args):
        self.driver = None
        self.headless = False

        if len(args) > 1:
            if '-hl' in args:
                self.headless = True
            if '-b' in args:
                self.driver = args[args.index('-b')+1]
            if '--browser' in args:
                self.driver = args[args.index('--browser')+1]

    def open_browser(self):
        if self.driver != None:
            if self.driver.lower() == "chrome":
                super().chosen_browser('chrome')

                options = webdriver.ChromeOptions()
                if self.headless:
                    super().pretty("Running in headless")
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')

                self.browser = webdriver.Chrome(chrome_options=options)

            elif self.driver.lower() == "opera":
                super().chosen_browser('opera')
                self.browser = webdriver.Opera()

            elif self.driver.lower() == "firefox":
                super().chosen_browser('firefox')
                options = webdriver.FirefoxOptions()
                if self.headless:
                    super().pretty("Running in headless")
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                self.browser = webdriver.Firefox(firefox_options=options)

            elif self.driver.lower() == "safari":
                super().chosen_browser('safari')
                self.browser = webdriver.Safari()
                
            elif self.driver.lower() == "edge":
                super().chosen_browser('edge')
                self.browser = webdriver.Edge()

            elif self.driver.lower() == "ie":
                super().chosen_browser('ie')
                self.browser = webdriver.Ie()

            else:
                super().warning("Please provide supported browser.\nrun the command with [-h or --help] flag to get all the list of supported browsers.")
                sys.exit()
        else:
            super().chosen_browser('chrome')

            options = webdriver.ChromeOptions()
            if self.headless:
                super().pretty("Running in headless")
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                
            self.browser = webdriver.Chrome(chrome_options=options)
