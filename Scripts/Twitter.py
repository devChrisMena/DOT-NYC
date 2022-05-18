from ast import Tuple
import csv
from fileinput import filename
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementNotInteractableException, ElementClickInterceptedException, SessionNotCreatedException, WebDriverException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import datetime
import pandas as pd

# constans and variables
DELAY = 7
data = []
tweet_ids = set()

def setDay(value):
    range = datetime.datetime.now() - datetime.timedelta(days=int(value))
    return range

def getTweetData(card) -> Tuple:
    """
    Extract data from tweet data.
    Takes a tweet card  Selenium WebElement as a parameter
    """
    username = loadElement(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]//a', card).text
    handle = loadElement(By.XPATH, './/span[contains(text(), "@")]', card).text
    try:
        postdate = loadElement(By.XPATH, '//time', card).get_attribute('datetime')
    except NoSuchElementException:
        return
    except StaleElementReferenceException:
        return
    comment = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
    #response = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]').text
    text = comment
    reply_count = loadElement(By.XPATH, './/div[@data-testid="reply"]', card).text
    retweet_count = loadElement(By.XPATH, './/div[@data-testid="retweet"]', card).text
    like_count = loadElement(By.XPATH, './/div[@data-testid="like"]', card).text
    #replying_to = loadElement(By.XPATH, './')
    post_rate = ''
    tweet = (username, handle, postdate, text)
    return tweet

def loadElement(by, path, browser):
    """
    Given a By and Path, load element
    Returns WebElement
    """
    try:
        element = WebDriverWait(browser, DELAY).until((EC.presence_of_element_located((by, path))))
        return element
    except TimeoutError:
        return None

def loadElements(by, path, browser):
    """
    Given a By and Path, load elements
    Returns a list of WebElements
    """
    try:
        elements = WebDriverWait(browser, DELAY).until((EC.presence_of_all_elements_located((by, path))))
        return elements
    except TimeoutError:
        return None

def formatTime(data_time):
    """
    Function formats a given date 
    """
    dt = datetime.datetime(int(data_time[:4]), int(
        data_time[5:7]), int(data_time[8:10]))
    return dt

def login(user_name, user_pass, driver):
    username = loadElement(By.XPATH, '//input[@name="text"]', driver)
    username.send_keys(user_name)
    username.send_keys(Keys.RETURN)
    sleep(1)
    password = loadElement(By.XPATH, '//input[@name="password"]', driver)
    password.send_keys(user_pass)
    password.send_keys(Keys.RETURN)

def searchFor(target, driver):
    # searching
    search = loadElement(By.XPATH, '//input[@placeholder="Search Twitter"]', driver)
    search.send_keys(target)
    search.send_keys(Keys.RETURN)
    return search

def start(value):
    target_datetime = setDay(value)

    # create instance of webdriver
    try:
        driver = Chrome()
    except SessionNotCreatedException:
        print('Update Chrome webdriver!!')
    except WebDriverException:
        print('No webdriver found')
        return
    sleep(1)

    # navigate to login screen
    driver.get('https://www.twitter.com/login')
    driver.maximize_window()

    login('bot_intern42', 'internbot42', driver)
    search = searchFor('@NYC_DOT', driver)

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
                if tweet_id not in tweet_ids and tweet[3] != None or tweet[3] != '':
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
            sleep(1.5)
            current_position = driver.execute_script('return window.pageYOffset;')
            if last_position == current_position:
                scroll_attempt += 1
                # end scrolling
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    sleep(1.5)
            else:
                last_position = current_position
                break
    driver.close()

    # saving data
    date_filename = 'Twitter_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv' 
    with open(date_filename, 'w', newline='', encoding='utf-8') as f:
        header = ['UserName', 'Handle', 'Timestamp', 'Comments']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('Done')

    csv_file = pd.read_csv(date_filename, index_col=0)
    csv_file.dropna(subset=["Comments"], inplace=True)
    csv_file.to_csv(date_filename)

if __name__ == "__main__":
    start(value = 5)