from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains, ChromeOptions
import getpass
import sys
import os
from colorama import Fore

APP_NAME = "AUTO LIKE INSTA POST"
username = ""
password = ""
internetTime = 5
driver = None
URL = 'https://www.instagram.com/'

def take_user_info():
    global username 
    username = input("Enter your username: ").lower()
    global password 
    password = input("Enter instagram password: ")
    if password == "" or username == "":
        print(f"{Fore.RED}Password and username both fields are required.{Fore.RESET}")
        take_user_info()

try:
    os.system("clear")
    args = sys.argv
    if '-h' in args or '--help' in args:
            print(f"""
help for {APP_NAME}.\n
help        -h  --help open help for {APP_NAME}.
browser     -b <option> --browser <option> set browser. 
            """)
            sys.exit()
    
    print(f"""{Fore.YELLOW}_____________________________________________________
|                                                   |
|         #######      LIKE INSTA POST              |
|        #### ####     @hi.coders                   |
|       ###  #  ###    ###   ### ####### #######    |
|      ###  ###  ###   ###   ###   ###   ##   ##    |
|     ##   #####   ##  ###   ###   ###   ##   ##    |
|    ##   #######   ## #########   ###   #######    |
|___________________________________________________|{Fore.RESET}
""")

    if len(args) > 2:
        if '-b' in args:
            driver = args[args.index('-b')+1]
        if '--browser' in args:
            driver = args[args.index('--browser')+1]
    take_user_info()

    userTime = input("What your average website loading time [second](optional): ")
    pages = input('Number of page to scroll [default=2](optional): ')
    
    if pages == "":
        pages = '2'

    if userTime != "" and pages != "":
        internetTime = float(userTime)
    estTime = (int(pages) * 2) + internetTime + (internetTime * 1.5) + (internetTime * 1.3) + 1 + 2
    print(f"{Fore.MAGENTA}Estimated time to like:{Fore.RESET} {Fore.GREEN}{str(estTime) + ' second' if estTime < 60  else str(estTime / 60) + ' minute' }{Fore.RESET}")

    if driver != None:
        if driver.lower() == "chrome":
            print(f"{Fore.BLUE}Opening Browser: chrome{Fore.RESET}")
            browser = webdriver.Chrome()
        if driver.lower() == "opera":
            print(f"{Fore.BLUE}Opening Browser: opera{Fore.RESET}")
            browser = webdriver.Opera()
        if driver.lower() == "firefox":
            print(f"{Fore.BLUE}Opening Browser: firefox{Fore.RESET}")
            browser = webdriver.Firefox()
        if driver.lower() == "safari":
            print(f"{Fore.BLUE}Opening Browser: safari{Fore.RESET}")
            browser = webdriver.Safari()
        if driver.lower() == "ie":
            print(f"{Fore.BLUE}Opening Browser: ie{Fore.RESET}")
            browser = webdriver.Ie()
    else:
        print(f"{Fore.BLUE}Opening Browser: chrome{Fore.RESET}")
        browser = webdriver.Chrome()
    
    print(f"{Fore.MAGENTA}Navigating to{Fore.RESET} {Fore.CYAN}{URL}{Fore.RESET}")
    browser.get(URL)

    print(f'{Fore.GREEN}waiting for {internetTime} second{Fore.RESET}')
    sleep(internetTime)

    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username+Keys.TAB)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    browser.execute_script("document.querySelector(\"#loginForm > div > div:nth-child(3) > button\").click()")

    print(f'{Fore.YELLOW}Loging into @{username}...{Fore.RESET}')
    print(f'{Fore.GREEN}waiting for {internetTime * 1.5} second{Fore.RESET}')
    sleep(internetTime * 1.5)

    print(f"{Fore.YELLOW}Navgating to feed page...{Fore.RESET}")
    browser.execute_script('document.querySelector("#react-root > section > main > div > div > div > div > button").click()')

    print(f'{Fore.GREEN}waiting for {internetTime * 1.3} second{Fore.RESET}')
    sleep(internetTime * 1.3)
    try:
        browser.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()')
    except Exception as notification:
        print(f"{Fore.RED}Notification dialog not closed{Fore.RESET}")

    sleep(1)

    print(f'{Fore.YELLOW}Started liking {Fore.RED}♥{Fore.YELLOW} process')
    browser.execute_script("""
        const like = () => {
            let articles = document.querySelectorAll(
                "#react-root > section > main > section > div > div:nth-child(2) > div > article > div > section > span > button > div > span > svg"
            );
            articles.forEach((article) => {
                let label = article.getAttribute("aria-label");
                if (label === "Like") {
                    article.parentElement.parentElement.parentElement.click();
                }
            });
        };
        like();
        let currentPage = 1;
        let totalPageToLoad = """ + pages +""";
        const loadPage = () => {
            if(currentPage <= totalPageToLoad) {
                setTimeout(() => {
                    document
                        .querySelector("html")
                        .scrollTo(
                            0,
                            document.querySelector("html").scrollTop +
                                (document.querySelector("html").scrollHeight / 100) *
                                    20
                        );
                    like();
                    loadPage();
                    currentPage += 1;
                }, 1500);
            }
        }
        loadPage();
    """)
    sleep(int(pages) * 2)
    print("Done: exiting all the processes")
    print(f"{Fore.BLUE}Bye{Fore.RESET}")
    browser.close()
except Exception as e:
    print(f"{Fore.RED}Error occurs")
    print(e)
    Fore.RESET