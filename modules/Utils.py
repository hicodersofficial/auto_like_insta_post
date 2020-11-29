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
help          -h  --help open help for {APP_NAME}.
browser       -b <option> --browser <option> opens your favorite browser. supported browsers [chrome, firefox, safari, edge, ie]. 
load time     -lt <second> average loading time for web.
scroll pages  -sp <number> of page to scroll and like
headless      -hl runs browser in headless mode. supported headless browsers are [chrome, firefox]
user          -u <username> likes all post of the users from your account.
follow        -f [-u <username> -f <true>] include -f true flag to follow user and like. 
message       -m [-m <message> -u <username> ] send message to username provided.
message limit -ml <number> message limit to send.
MTI           -mti  <millisecond> MIT or message typing interval is typing interval between each character in millisecond.
MII           -mii include this flag if you want to send message sent index(number). eg [1 hi, 2 hi]
MI            -mi <second> include this flag if you want to wait each time before sending message. (interval for each message in second)
            """)
            sys.exit()

    def print_name(self):
         print(f"""{Fore.YELLOW}
________________________________________________________
|                                                      |
|         #######         ### ##   #  ### ###    #     |
|        #### ####         #  # #  # ##    #    # #    |
|        ( *   * )         #  #  # #   ##  #   # # #   |
|       ###  #  ###       ### #   ## ###   #  #     #  |
|      ###  ###  ###      @hi.coders @priyanshu_raz_z  |
|     ##           ##     ###   ###  #######  #######  |
|    ##   #######   ##    ###   ###    ###    ##   ##  |
|   ##   #########   ##   ###   ###    ###    ##   ##  |
|  ##   ###########   ##  #########    ###    #######  |
|______________________________________________________|{Fore.RESET}""")
