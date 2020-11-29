from colorama import Fore
import sys
class Display:

    def __init__(self):
        pass

    def stats_estimated_time(self, estTime):
        print(f"{Fore.MAGENTA}Estimated time to like:{Fore.RESET} {Fore.GREEN}{str(estTime) + ' second' if estTime < 60  else str(estTime / 60) + ' minute' }{Fore.RESET}")
    

    def chosen_browser(self, browser):
        print(f"{Fore.BLUE}Opening Browser: {browser}{Fore.RESET}")

    def warning(self, msg):
        print(f"{Fore.RED}{msg}{Fore.RESET}")

    def navigating_url(self, URL):
        print(f"{Fore.MAGENTA}Navigating to{Fore.RESET} {Fore.CYAN}{URL}{Fore.RESET}")

    def account(self, username):
         print(f'{Fore.YELLOW}Loging into @{username}...{Fore.RESET}')

    def wait_time(self, time):
        print(f'{Fore.GREEN}waiting for {time} second{Fore.RESET}')

    def feed_nav(self):
        print(f"{Fore.YELLOW}Navgating to feed page...{Fore.RESET}")
    
    def closing(self):
        print(f"{Fore.YELLOW}Done: exiting all the processes{Fore.RESET}")
        print(f"{Fore.BLUE}Bye{Fore.RESET}")
    
    def pretty(self, msg):
        print(f"{Fore.BLUE}{msg}{Fore.RESET}")
    def exit(self, msg):
        print(f"{Fore.RED}{msg}{Fore.RESET}")
        sys.exit()