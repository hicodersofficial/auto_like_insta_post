# AUTO LIKE INSTA POST (BOT)

simple auto liking instagram posts.

This app can like your feed posts or single user posts.

### Install requirements.txt

> make sure to have selenium drivers for the browsers in **PATH**.

```
$ pip install -r requirements.txt
```

### Run

run the app just by running the following command.

The below command like your feed posts.

```
$ python main.py
```

Follow user and likes his all post by running following command.

> If you don't want to follow the user but want to just like his post then omit the "`-f true`" flag

```
$ python main.py -u rollsroycecars -f true
```

Send message to the user.

```
$ python main.py -m hello -u hi.coders -ml 10
        or
$ python main.py -m "hello" -u hi.coders -ml 10 -mii -mti 50 -mi 1
```

## Supported browsers

-   chrome
-   firefox
-   opera
-   safari
-   Edge
-   IE

```
$ python main.py -b firefox
$ Enter your username: YOUR_USERNAME
$ Enter instagram password: YOUR_PASSWORD
```

### Help for app.

open help for the app.

```
$ python main.py --help
```

```
help for AUTO LIKE INSTA POST.

help          -h  --help open help for AUTO LIKE INSTA POST.
browser       -b <option> --browser <option> opens your favorite browser.
              supported browsers [chrome, firefox, safari, edge, ie].
load time     -lt <second> average loading time for web.
scroll pages  -sp <number> of page to scroll and like
headless      -hl runs browser in headless mode.
              supported headless browsers are [chrome, firefox]
user          -u <username> likes all post of the users from your account.
hashtag       -ht likes all the post of hashtag. <-u hashtag -ht>
follow        -f [-u <username> -f <true>] include -f true flag to follow user and like.
message       -m [-m <message> -u <username> ] send message to username provided.
message limit -ml <number> message limit to send.
MTI           -mti  <millisecond> MIT or message typing interval is
                    typing interval between each character in millisecond.
MII           -mii include this flag if you want to send message sent index(number). eg [1 hi, 2 hi]
MI            -mi <second> include this flag if you want to wait each time before sending message.
              (interval for each message in second)
```

### Selenium browser webdriver

download drivers for your browser.

-   chrome [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home)
-   firefox [geckodriver](https://github.com/mozilla/geckodriver/releases)
-   opera [OperaChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/home)
-   safari [SafariDriver](https://developer.apple.com/safari/download/)
-   Edge [edgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
-   IE [IEDriverServer](http://selenium-release.storage.googleapis.com/index.html)

## Screenshot

![](./Screenshot.png)

## Thank You 🙏
