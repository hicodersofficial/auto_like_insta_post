from time import sleep
from modules.Display import Display
from config.global_variables import URL
from config.scripts import CLICK_MESSAGE_BUTTON, CLOSE_NOTIFICATION_DIALOG, MESSAGE_TEXTAREA_XPATH, MESSAGE_SEND_BUTTON_XPATH
from selenium.webdriver.common.keys import Keys

class Message(Display):
    def __init__(self, args):

        # username of the user whom message has to send.
        self.username = None

        # wait for each message after sending (in second)
        self.msg_time_interval = 0

        # limit of the message to send to the user.
        self.message_limit = 1

        # message to send.
        self.message = 'Hi'

        # include index for each message.
        self.include_index=False

        # perform typing interval is the time in millisecond between each key stroke.
        self.perform_typing_interval = None
        
        if '-m' in args and '-u' in args and '-mii' in args:
            self.include_index=True

        if '-m' in args and '-u' and '-mti' in args:
            try:
                self.perform_typing_interval = int(args[args.index('-mti')+1])
            except Exception as e:
                super().exit("Invalid arguments. Please provide message typing interval(seconds) -mti <interval>")

        if '-m' in args and '-u' and '-mi' in args:
            try:
                self.msg_time_interval = int(args[args.index('-mi') + 1])
            except Exception as e:
                super().exit("Invalid arguments. Please provide message interval(seconds) -mi <interval>")

        if '-m' in args and '-u' in args:
            try:
                self.username = args[args.index('-u')+1]
            except Exception as e:
                super().exit("Invalid arguments. username should provided -u <username>")
            try:
                self.message = args[args.index('-m')+1]
            except Exception as e:
                 super().exit("Invalid arguments. message should provided -u <message>")

            if '-m' in args and '-u' and '-ml' in args:
                try:
                    self.message_limit = int(args[args.index('-ml') + 1])
                except Exception as e:
                    super().exit("Invalid arguments. Please provide message limit(number) -ml <limit>")


    # sendMessage() method
    # Navigate to the user and revoke send method to send message.
    def sendMessage(self, internetTime, browser):
        if self.username:
            browser.get(f"{URL}{self.username}")

            super().wait_time((internetTime / 100) * 20)
            sleep((internetTime / 100) * 20)

            browser.execute_script(CLICK_MESSAGE_BUTTON)

            super().wait_time(internetTime)
            sleep(internetTime)

            try:
                browser.execute_script(CLOSE_NOTIFICATION_DIALOG)
                super().pretty("Closed notification dialog box")
            except Exception as e:
                pass

            super().pretty("Started sending...")

            # loop till the message limit.
            for i in range(1, self.message_limit + 1):
                self.send(browser, i)
                super().pretty(f"message sent: {i}")
                if self.message_limit != 0:
                    sleep(self.msg_time_interval)
            
            # prints closing lines
            super().closing()
            # closes browser
            browser.close()
    
    # send() method.
    # send message to the user
    def send(self, browser, index = 0):
        # message (include index if self.include_index === True )
        message = str(index) + " " + self.message if self.include_index else self.message

        # perform typing interval like human hand.
        if self.perform_typing_interval:
            for latter in message:
                browser.find_element_by_xpath(MESSAGE_TEXTAREA_XPATH).send_keys(latter)
                sleep(self.perform_typing_interval/1000)
        else:
            browser.find_element_by_xpath(MESSAGE_TEXTAREA_XPATH).send_keys(message)
        
        # click send button.
        browser.find_element_by_xpath(MESSAGE_SEND_BUTTON_XPATH).click()
