
from json import load
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ast import Tuple
from getpass import getpass
from time import sleep
import csv
import selenium 

# Constants and Functions
DELAY = 15

def loadElement(by, path, browser):
    """
    Given a By and Path, load element
    Returns WebElement
    """
    try:
        element = WebDriverWait(browser, DELAY).until((EC.presence_of_element_located((by, path))))
        print('Page is read!')
        return element
    except TimeoutError:
        print('Page too long to load ')
        return None

def loadElements(by, path, browser):
    """
    Given a By and Path, load elements
    Returns a list of WebElements
    """
    try:
        element = WebDriverWait(browser, DELAY).until((EC.presence_of_all_elements_located((by, path))))
        print('Page is read!')
        return element
    except TimeoutError:
        print('Page too long to load ')
        return None
    except TimeoutException:
        print('Page too long to load ')
        return None
def getPostData(post) -> Tuple:
    """
    Extract data from post data.
    Takes a post Selenium WebElement as a parameter
    """
    print('Inside getDataPost')
    user_name = loadElement(By.XPATH, './div[1]/li[1]/div[1]/div[1]/div[2]//h3', post).text
    user_comment = loadElement(By.XPATH, './div[1]/li[1]/div[1]/div[1]/div[2]/div[1]/span', post).text
    reply_usernames = []
    reply_user_comments = []

    print((user_name, user_comment, reply_usernames, reply_user_comments))
    post_data = (user_name, user_comment, reply_usernames, reply_user_comments)
    print('Exiting getDataPost')
    return post_data

def loadMoreComments(path, driver):
    print('Inside loadMoreComments')
    print('Inside loading')
    try:
        load = loadElement(By.XPATH, path, driver)
    except NoSuchElementException:
        print('Button not present, exiting')
        loading = False
    else:
        print('Button is present')
        load.click()
        return

# create instance of webdriver
#driver = Chrome('/Users/christophermena/Downloads/chromedriver')
driver = Chrome()
sleep(1)

# navigate to login screen
driver.get('https://www.instagram.com/')
driver.maximize_window()


username = loadElement(By.XPATH, '//input[@name="username"]', driver)
username.send_keys('')

password = loadElement(By.XPATH, '//input[@name="password"]', driver)
password.send_keys('')
password.send_keys(Keys.RETURN)

save_btm = loadElement(By.XPATH, '//div[@class="cmbtv"]', driver).click()
notification_btn = loadElement(By.XPATH, '//div[@class="mt3GC"]', driver).click()

search = loadElement(By.XPATH, '//div[@class=" cTBqC"]', driver).click()
search = loadElement(By.XPATH, '//input[@placeholder="Search"]', driver)
search.send_keys('@nyc_dot')

dotpage = loadElement(By.XPATH, '//a[@href="/nyc_dot/"]', driver).click()
page = loadElement(By.XPATH, '//article[@class="ySN3v"]', driver)
articles = loadElement(By.XPATH, '//article[@class="ySN3v"]', driver)
strips_posts = loadElements(By.XPATH, '//div[@class="Nnq7C weEfm"]', articles)
data = []

for strip in strips_posts:
    print(data)
    posts = loadElements(By.XPATH, './/div[@class="v1Nh3 kIKUG _bz0w"]', strip)
    for post in posts:
        post.click()
        post_content = loadElement(By.XPATH, '//div[@class="RnEpo   _Yhr4     "]', driver)
        close_post = loadElement(By.XPATH, './div[1]/button', post_content)
        post_texts = loadElements(By.XPATH, './/ul[@class="Mr508 "]', post_content)
        #loadMoreComments('button[@class="wpO6b  "]', post_content)
        if post_texts != None:
            for text_data in post_texts:
                data.append(getPostData(text_data))
            close_post.click()
