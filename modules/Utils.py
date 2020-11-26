import sys
from config.global_variables import APP_NAME
from colorama import Fore

class Utils:
    def __init__(self, args):
        self.args = args
        if '-h' in self.args or '--help' in self.args:
            self.app_help()
            
    def app_help(self):
            print(f"""
help for {APP_NAME}.\n
help        -h  --help open help for {APP_NAME}.
browser     -b <option> --browser <option> set browser. 
user        -u <username> likes all post of the users from your account.
follow      -f [-u <username> -f <true>] include -f true flag to follow user and like. 
            """)
            sys.exit()

    def print_name(self):
         print(f"""{Fore.YELLOW}
_____________________________________________________
|                                                   |
|         #######      LIKE INSTA POST              |
|        #### ####     @hi.coders                   |
|       ###  #  ###    ###   ### ####### #######    |
|      ###  ###  ###   ###   ###   ###   ##   ##    |
|     ##   #####   ##  ###   ###   ###   ##   ##    |
|    ##   #######   ## #########   ###   #######    |
|___________________________________________________|{Fore.RESET}
""")
