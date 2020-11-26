USERNAMETEXTBOX_X_PATH = '//*[@id="loginForm"]/div/div[1]/div/label/input'
PASSWORDTEXTBOX_X_PATH = '//*[@id="loginForm"]/div/div[2]/div/label/input'
SUBMITBUTTON_CSS_SELECTOR = 'document.querySelector("#loginForm > div > div:nth-child(3) > button").click()'

def USER_FEED_LIKE(pages):
    return """
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
"""

CLOSE_SAVING_DIALOG='document.querySelector("#react-root > section > main > div > div > div > div > button").click()'

CLOSE_NOTIFICATION_DIALOG='document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()'



SINGLE_USER_POST_LIKE="""
    let i = 0;
    function like() {
        let posts = document.querySelectorAll(
            "#react-root > section > main > div > div._2z6nI > article > div > div > div > div > a"
        );
        posts[i].click();
        if (i !== 0 && i % 21 === 0) {
            document
                .querySelector("html")
                .scrollTo(0, document.querySelector("html").scrollHeight);
        }
        setTimeout(() => {
            if (
                document.querySelector(
                    "body > div > div > div > article > div> div > div > div"
                )
            ) {
                try {
                    let label = document
                        .querySelector(
                            "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg"
                        )
                        .getAttribute("aria-label");
                    if (label === "Like") {
                        document
                            .querySelector(
                                "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button"
                            )
                            .click();
                    }
                    setTimeout(() => {
                        document
                            .querySelector(
                                "body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button"
                            )
                            .click();
                        if (i !== posts.length) {
                            like();
                        } else {
                            alert("Task compeleted. total post liked " + parseInt(i + 1));
                        }
                    }, 500);
                } catch (error) {
                    if (
                        error.message ===
                        "Cannot read property 'getAttribute' of null"
                    ) {
                        like();
                        return;
                    }
                }
            } else {
                console.log("Your inter seems slow.");
                like();
                return;
            }
            i += 1;
        }, 2000);
    }
    like();
"""

FOLLOW_SCRIPT='''
    try {
        let node = document.querySelector("#react-root > section > main > div > header > section > div > div > div > div> div > span > span > button > div > span")

        node = node ? node : document.querySelector("#react-root > section > main > div > header > section > div > div > div > div>  button > div > span")
        
        if(node && node.getAttribute("aria-label") == "Following") { 
            console.log("You had already followed") 
        } else {
            document.querySelector("#react-root > section > main > div > header > section > div > div > div  button").click()
        }
    }
    catch(error) {
        console.log(error + " :insta auto like")
    }
'''