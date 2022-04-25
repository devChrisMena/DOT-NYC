from ast import Tuple
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
import datetime

# constans and variables
DELAY = 7
data = []
tweet_ids = set()
target_datetime = datetime.datetime.now(
) - datetime.timedelta(days=int(input('Enter number of days: ') or '30'))

def getTweetData(card) -> Tuple:
    """
    Extract data from tweet data.
    Takes a tweet card  Selenium WebElement as a parameter
    """
    username = card.find_element(by=By.XPATH, value='./div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]//a').text
    handle = card.find_element(by=By.XPATH, value='.//span[contains(text(), "@")]').text
    try:
        postdate = card.find_element(By.XPATH, '//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    except StaleElementReferenceException:
        return
    comment = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
   # response = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]').text
    text = comment
    reply_count = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    retweet_count = card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
    like_count = card.find_element(By.XPATH, './/div[@data-testid="like"]').text
    
    tweet = (username, handle, postdate, text, reply_count, retweet_count, like_count)
    return tweet

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
driver.get('https://www.twitter.com/login')
driver.maximize_window()

username = loadElement(By.XPATH, '//input[@name="text"]', driver)
username.send_keys('iamcriss_1')
username.send_keys(Keys.RETURN)

my_password = 'Criss195!'
password = loadElement(By.XPATH, '//input[@name="password"]', driver)
password.send_keys(my_password)
password.send_keys(Keys.RETURN)

# searching

search = loadElement(By.XPATH, '//input[@placeholder="Search Twitter"]', driver)
search.send_keys('@DOT')
search.send_keys(Keys.RETURN)

# naviagte to lastest tap
lastest = loadElement(By.LINK_TEXT, 'Latest', driver).click()

last_position = driver.execute_script('return window.pageYOffset;')
scrolling = True

sleep(7)
# scroll down page
while scrolling:
    # load tweets
    page_cards = loadElements(By.XPATH, '//article[@data-testid="tweet"]', driver) 
    for card in page_cards[-15:]:
        tweet = getTweetData(card)
        if tweet:
            # create unique tweet id
            tweet_id = ''.join(tweet)
            date = tweet[2]
            date_pass = not(target_datetime > formatTime(date))
            # if id not in tweet_ids
            if tweet_id not in tweet_ids:
                # add it to tweet_ids
                tweet_ids.add(tweet_id)
                data.append(tweet)
            if date_pass:
                continue
                print(date)
            else:
                scrolling = False
                break
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
with open('tweet_data.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Handle', 'Timestamp', 'Comments', 'Likes', 'Retweets', 'Text']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print('Done')