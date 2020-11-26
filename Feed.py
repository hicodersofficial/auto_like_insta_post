from Browser import Browser
from colorama import Fore
from time import sleep
from Display import Display
from scripts import USER_FEED_LIKE, CLOSE_NOTIFICATION_DIALOG, CLOSE_SAVING_DIALOG

class Feed(Display):
    def __init__(self):
        pass

    def like(self, browser, internetTime, pages):
        super().feed_nav()
        browser.execute_script(CLOSE_SAVING_DIALOG)
        super().wait_time(internetTime * 1.3)
        sleep(internetTime * 1.3)
        try:
            browser.execute_script(CLOSE_NOTIFICATION_DIALOG)
        except Exception as notification:
            print(f"{Fore.RED}Notification dialog not closed{Fore.RESET}")
        sleep(1)
        print(f'{Fore.YELLOW}Started liking {Fore.RED}♥{Fore.YELLOW} process')
        browser.execute_script(USER_FEED_LIKE(pages))
        sleep(int(pages) * 2)
        super().closing()
        browser.close()