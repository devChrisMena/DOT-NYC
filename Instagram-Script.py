
from json import load
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from ast import Tuple
from getpass import getpass
from time import sleep
import csv
import selenium 
import datetime

# Constants and Functions
DELAY = 15

target_datetime = datetime.datetime.now(
) - datetime.timedelta(days=int(input('Enter number of days: ') or '30'))

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
    except StaleElementReferenceException:
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
    except StaleElementReferenceException:
        return None
def getPostData(post) -> Tuple:
    """
    Extract data from post data.
    Takes a post Selenium WebElement as a parameter
    """
    print('Inside getDataPost')
    user_name = loadElement(By.XPATH, './div[1]/li[1]/div[1]/div[1]/div[2]//h3', post).text
    user_comment = loadElement(By.XPATH, './div[1]/li[1]/div[1]/div[1]/div[2]/div[1]/span', post).text
    time = loadElement(By.XPATH, '//time', post).get_attribute('datetime')
    reply_usernames = []
    reply_user_comments = []

    print((user_name, user_comment, reply_usernames, reply_user_comments))
    post_data = (user_name, user_comment, reply_usernames, reply_user_comments, time)
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

def formatTime(data_time):
    """
    Function formats a given date 
    """
    dt = datetime.datetime(int(data_time[:4]), int(
        data_time[5:7]), int(data_time[8:10]))
    return dt

# create instance of webdriver
#driver = Chrome('/Users/christophermena/Downloads/chromedriver')
driver = Chrome()
sleep(1)

# navigate to login screen
driver.get('https://www.instagram.com/')
driver.maximize_window()


username = loadElement(By.XPATH, '//input[@name="username"]', driver)
username.send_keys('iamcriss_1')

password = loadElement(By.XPATH, '//input[@name="password"]', driver)
password.send_keys('titi020696')
password.send_keys(Keys.RETURN)

save_btm = loadElement(By.XPATH, '//div[@class="cmbtv"]', driver).click()
notification_btn = loadElement(By.XPATH, '//div[@class="mt3GC"]', driver).click()

search = loadElement(By.XPATH, '//div[@class=" cTBqC"]', driver).click()
search = loadElement(By.XPATH, '//input[@placeholder="Search"]', driver)
search.send_keys('@nyc_dot')

dotpage = loadElement(By.XPATH, '//a[@href="/nyc_dot/"]', driver).click()
page = loadElement(By.XPATH, '//article[@class="ySN3v"]', driver)
articles = loadElement(By.XPATH, '//article[@class="ySN3v"]', driver)
data = []

last_position = driver.execute_script('return window.pageYOffset;')
scrolling = True
post_ids = set()

while scrolling:
    strips_posts = loadElements(By.XPATH, '//div[@class="Nnq7C weEfm"]', articles)
    if strips_posts == None:
        scrolling = False
        break
    for strip in strips_posts[-15:]:
        print(data)
        posts = loadElements(By.XPATH, './/div[@class="v1Nh3 kIKUG _bz0w"]', strip)
        if posts == None:
            scrolling = False
            break
        for post in posts:
            try:
                post.click()
            except ElementNotInteractableException:
                post_content = loadElement(By.XPATH, '//div[@class="RnEpo   _Yhr4     "]', driver)
                close_post = loadElement(By.XPATH, './div[1]/button', post_content)
                close_post.click()
                break
            except ElementClickInterceptedException:
                post_content = loadElement(By.XPATH, '//div[@class="RnEpo   _Yhr4     "]', driver)
                close_post = loadElement(By.XPATH, './div[1]/button', post_content)
                close_post.click()
                break
            post_content = loadElement(By.XPATH, '//div[@class="RnEpo   _Yhr4     "]', driver)
            close_post = loadElement(By.XPATH, './div[1]/button', post_content)
            post_texts = loadElements(By.XPATH, './/ul[@class="Mr508 "]', post_content)
            #loadMoreComments('button[@class="wpO6b  "]', post_content)
            if post_texts != None:
                for text_data in post_texts:
                    post_data = getPostData(text_data)
                    if post_data:
                        post_id = ''.join(post_data[0])
                        if post_id not in post_ids:
                            date = post_data[4]
                            date_pass = not(target_datetime > formatTime(date))
                            if date_pass:
                                post_ids.add(post_id)
                                data.append(post_data)
                close_post.click()
    # scroll attempt
    scroll_attempt = 0
    while True:
        # scroll down page
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')   
        sleep(3)
        current_position = driver.execute_script('return window.pageYOffset;')
        if last_position == current_position:
            scroll_attempt += 1
            # end scrolling
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                sleep(3)
        else:
            last_position = current_position
            break

driver.close()

# saving data
# (user_name, user_comment, reply_usernames, reply_user_comments)
with open('post_data.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Comment', 'Reply-Usernames', 'Reply-User-Comments']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print('Done')