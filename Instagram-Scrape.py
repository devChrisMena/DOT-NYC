
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
def getPostData(post):
    """
    Extract data from instagram data.
    Takes a post card  Selenium WebElement as a parameter
    """
    post.find_element(By.XPATH, './/a').click()
    sleep(3)
    post_content = post.find_element(By.XPATH, '//div[@role="presentation"]')
    try:
        username = post_content.find_element(
            By.XPATH, './/h2[@class="_6lAjh "]').text
    except NoSuchElementException:
        return
    comment = post_content.find_element(
        By.XPATH, './/span[@class="_7UhW9   xLCgt      MMzan   KV-D4            se6yk       T0kll "]').text
    time = post_content.find_element(
        By.XPATH, './/time[@class="_1o9PC"]').get_attribute('datetime')
    time = time[:10]
    # close post
    post_content.find_element(By.XPATH, './/button[@class="wpO6b  "]').click()
    sleep(1)
    content = (username, comment, time)
    return content

def loadElement(by, path, browser):
    """
    Given a By and Path, load element
    """
    try:
        element = WebDriverWait(browser, DELAY).until((EC.presence_of_element_located((by, path))))
        print('Page is read!')
        return element
    except TimeoutException:
        print('Page too long to load ')
        return None

def loadElements(by, path, browser):
    """
    Given a By and Path, load element
    """
    try:
        element = WebDriverWait(browser, DELAY).until((EC.presence_of_all_elements_located((by, path))))
        print('Page is read!')
        return element
    except TimeoutException:
        print('Page too long to load ')
        return None

def formatTime(data_time):
    """
    Function formats a given date 
    """
    dt = datetime.datetime(int(data_time[:4]), int(
        data_time[5:7]), int(data_time[8:]))
    return dt


# create driver windows
driver = Chrome()
# mac
#driver = Chrome('/Users/christophermena/Downloads/chromedriver')
driver.get('https://www.instagram.com/')

# Login
username = loadElement(By.XPATH, '//input[@name="username"]', driver)
username.send_keys('iamcriss_1')
password = loadElement(By.XPATH, '//input[@name="password"]', driver)
password.send_keys('titi020696')
password.send_keys(Keys.RETURN)
save_btn = loadElement(By.XPATH, '//div[@class="cmbtv"]', driver).click()
notification_btn = loadElement(By.XPATH, '//div[@class="mt3GC"]', driver).click()

# Search
search = loadElement(By.XPATH, '//div[@class=" cTBqC"]', driver).click()
search = loadElement(By.XPATH, '//input[@placeholder="Search"]', driver)
search.send_keys('#nycdot')
search.send_keys(Keys.RETURN)
sleep(10)

# Page
dotpage = loadElement(By.XPATH, '//a[@href="/explore/tags/nycdot/"]', driver).click()
pages = loadElement(By.XPATH, '//article[@class="KC1QD"]', driver)
recent_pages = loadElements(By.XPATH, './div[2]/div[1]', pages)

# Data
data = []
post_ids = set()
last_position = driver.execute_script('return window.pageYOffset;')
scrolling = True
target_datetime = datetime.datetime.now(
) - datetime.timedelta(days=int(input('Enter number of days: ') or '30'))

# Scraping
while scrolling:
    # load post
    cards = loadElements(By.XPATH, './/div[@class="Nnq7C weEfm"]', recent_pages)
    for card in cards[-15:]:
        try:
            posts = loadElements(By.XPATH, './/div[@class="v1Nh3 kIKUG _bz0w"]', card)
        except StaleElementReferenceException:
            print('Error')
            break
        for post in posts:
            comment = getPostData(post)
            if comment:
                # create unique id
                post_id = ''.join(comment)
                # if id not in post_ids
                date = comment[2]
                date_pass = not(target_datetime > formatTime(date))
                if post_id not in post_ids:
                    post_ids.add(post_id)
                    data.append(comment)
                if date_pass:
                    continue
                else:
                    scrolling = False
                    break
    # scroll attempt
    scroll_attempt = 0
    while True:
        # scroll down page
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        sleep(3)
        current_position = driver.execute_script('return window.pageYOffset;')
        if last_position == current_position:
            scroll_attemtp += 1
            # end scrolling
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                sleep(3)
        else:
            last_position = current_position
            break

# saving data
with open('ig_data.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Comments', 'Time']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
