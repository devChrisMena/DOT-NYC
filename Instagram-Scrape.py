import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import datetime

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
    # close post
    post_content.find_element(By.XPATH, './/button[@class="wpO6b  "]').click()
    sleep(1)
    content = (username, comment, time)
    return content


# create driver windows
driver = Chrome()
sleep(5)
# mac
#driver = Chrome('/Users/christophermena/Downloads/chromedriver')
driver.get('https://www.instagram.com/')
sleep(5)
username = driver.find_element(By.XPATH, '//input[@name="username"]')
username.send_keys('iamcriss_1')
password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('titi020696')
password.send_keys(Keys.RETURN)
sleep(5)

save_btm = driver.find_element(By.XPATH, '//div[@class="cmbtv"]').click()
sleep(5)

notification_btn = driver.find_element(
    By.XPATH, '//div[@class="mt3GC"]').click()

search = driver.find_element(By.XPATH, '//div[@class=" cTBqC"]').click()
sleep(3)

search = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')

search.send_keys('#nycdot')

search.send_keys(Keys.RETURN)
sleep(5)

dotpage = driver.find_element(
    By.XPATH, '//a[@href="/explore/tags/nycdot/"]').click()
sleep(5)

pages = driver.find_element(By.XPATH, '//article[@class="KC1QD"]')
sleep(3)

recent_pages = pages.find_element(By.XPATH, './div[2]/div[1]')
sleep(3)

data = []
post_ids = set()
last_position = driver.execute_script('return window.pageYOffset;')
scrolling = True
current_datetime = datetime.datetime.now()



while scrolling:
    # load post
    cards = recent_pages.find_elements(
        By.XPATH, './/div[@class="Nnq7C weEfm"]')
    for card in cards[-15:]:
        try:
            posts = card.find_elements(
                By.XPATH, './/div[@class="v1Nh3 kIKUG _bz0w"]')
        except StaleElementReferenceException:
            print('Error')
            break

        for post in posts:
            comment = getPostData(post)
            if comment:
                # create unique id
                post_id = ''.join(comment)
                # if id not in post_ids
                if post_id not in post_ids:
                    post_ids.add(post_id)
                    data.append(comment)
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
