from global_variables import URL
from Display import Display
from time import sleep
from colorama import Fore
from scripts import FOLLOW_SCRIPT, SINGLE_USER_POST_LIKE

class Profile(Display):
    def __init__(self):
        pass

    def single_user_post_like(self, browser, args, internetTime, pages):
        username = None
        follow = None
        if '-u' in args:
            try:
                username = args[args.index('-u') + 1]
            except Exception as e:
                super().warning("Username required < -u username >")
        if '-f' in args  and '-u' in args and args[args.index('-f') + 1].lower() == 'true':
            follow = True

        if username:
            super().navigating_url(f"{URL}{username}")
            browser.get(f"{URL}{username}")
            super().wait_time(internetTime)
            sleep(internetTime)
            if(follow):
                super().pretty(f"followed @{username}")
                browser.execute_script(FOLLOW_SCRIPT)
            super().pretty(f"Started liking {Fore.RED}♥{Fore.YELLOW} @{username} posts.")
            browser.execute_script(SINGLE_USER_POST_LIKE)
            sleep(2)
            
        else:
            super().warning("Username required < -u username >")