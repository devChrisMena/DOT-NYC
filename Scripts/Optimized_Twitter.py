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


class Twitter:
    def __init__(self, username, password, days) -> None:
        self.username = username
        self.password = password
        self.days = days
        self.DELAY = 7
        self.data = []
        self.tweet_ids = set()
         # create instance of webdriver
        try:
            self.driver = Chrome()
        except SessionNotCreatedException:
            print('Update Chrome webdriver!!')
        except WebDriverException:
            print('No webdriver found')
        return
    sleep(1)

    def setDay(value):
        range = datetime.datetime.now() - datetime.timedelta(days=int(value))
        return range
    
    def getTweetData(card, self) -> Tuple:
        """
        Extract data from tweet data.
        Takes a tweet card  Selenium WebElement as a parameter
        """
        username = self.loadElement(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]//a', card).text
        handle = self.loadElement(By.XPATH, './/span[contains(text(), "@")]', card).text
        try:
            postdate = self.loadElement(By.XPATH, '//time', card).get_attribute('datetime')
        except:
            return
        comment = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
        #response = card.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]').text
        text = comment
        reply_count = self.loadElement(By.XPATH, './/div[@data-testid="reply"]', card).text
        retweet_count = self.loadElement(By.XPATH, './/div[@data-testid="retweet"]', card).text
        like_count = self.loadElement(By.XPATH, './/div[@data-testid="like"]', card).text
        #replying_to = loadElement(By.XPATH, './')
        post_rate = ''
        tweet = (username, handle, postdate, text)
        return tweet

    def loadElement(by, path, browser, self):
        """
        Given a By and Path, load element
        Returns WebElement
        """
        try:
            element = WebDriverWait(browser, self.DELAY).until((EC.presence_of_element_located((by, path))))
            return element
        except:
            return 

    def loadElements(by, path, browser, self):
        """
        Given a By and Path, load elements
        Returns a list of WebElements
        """
        try:
            elements = WebDriverWait(browser, self.DELAY).until((EC.presence_of_all_elements_located((by, path))))
            return elements
        except:
            return 

    def formatTime(data_time):
        """
        Function formats a given date 
        """
        dt = datetime.datetime(int(data_time[:4]), int(
            data_time[5:7]), int(data_time[8:10]))
        return dt

    def login(user_name, user_pass, driver, self):
        username = self.loadElement(By.XPATH, '//input[@name="text"]', driver)
        username.send_keys(user_name)
        username.send_keys(Keys.RETURN)
        sleep(1)
        password = self.loadElement(By.XPATH, '//input[@name="password"]', driver)
        password.send_keys(user_pass)
        password.send_keys(Keys.RETURN)

    def searchFor(target, driver, self):
        # searching
        search = self.loadElement(By.XPATH, '//input[@placeholder="Search Twitter"]', driver)
        search.send_keys(target)
        search.send_keys(Keys.RETURN)
        return search

    def start(self):
        target_datetime = self.setDay(self.days)

