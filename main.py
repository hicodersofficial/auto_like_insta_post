import os
import sys
from platform import platform
from global_variables import APP_NAME
from Browser import Browser
from Login import Login
from Utils import Utils
from Config import Config
from Feed import Feed
from Display import Display
from Profile import Profile

if __name__ == "__main__":
    display = Display()

    try:
        os.system("cls" if 'Windows' in platform() else 'clear')
        args = sys.argv
        utils = Utils(args)
        utils.print_name()
        login = Login()
        config = Config()
        config.estimated_time(display.stats_estimated_time)
        browser = Browser(args)
        login.login(browser.browser, config.internetTime)

        if '-u' in args:
            profile = Profile()
            profile.single_user_post_like(browser.browser, args, config.internetTime, config.pages)
        else:
            feed = Feed()
            feed.like(browser.browser, config.internetTime, config.pages)
        
    except Exception as e:
        display.warning("Error occurs"+str(e))