from ast import Tuple
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

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
    comment = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
   # response = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]').text
    text = comment
    reply_count = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    retweet_count = card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
    like_count = card.find_element(By.XPATH, './/div[@data-testid="like"]').text
    
    tweet = (username, handle, postdate, text, reply_count, retweet_count, like_count)
    return tweet

# create instance of webdriver
#driver = Chrome('/Users/christophermena/Downloads/chromedriver')
driver = Chrome()
sleep(1)

# navigate to login screen
driver.get('https://www.twitter.com/login')
driver.maximize_window()
sleep(2)

username = driver.find_element(by=By.XPATH, value='//input[@name="text"]')
username.send_keys('iamcriss_1')
username.send_keys(Keys.RETURN)
sleep(2)

my_password = 'Criss195!'
password = driver.find_element(by=By.XPATH, value='//input[@name="password"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)
sleep(2)

# searching
search = driver.find_element(by=By.XPATH, value='//input[@placeholder="Search Twitter"]')
search.send_keys('@NYC_DOT')
search.send_keys(Keys.RETURN)
sleep(2)

# naviagte to lastest tap
driver.find_element(by=By.LINK_TEXT, value='Latest').click()

# get all tweets on the page
data = []
tweet_ids = set()
last_position = driver.execute_script('return window.pageYOffset;')
scrolling = True

# scroll down page
while scrolling:
    # load tweets
    page_cards = driver.find_elements(by=By.XPATH, value='//article[@data-testid="tweet"]')
    for card in page_cards[-15:]:
        tweet = getTweetData(card)
        if tweet:
            # create unique tweet id
            tweet_id = ''.join(tweet)
            # if id not in tweet_ids
            if tweet_id not in tweet_ids:
                # add it to tweet_ids
                tweet_ids.add(tweet_id)
                data.append(tweet)
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

# saving data
with open('tweet_data.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['UserName', 'Handle', 'Timestamp', 'Comments', 'Likes', 'Retweets', 'Text']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)