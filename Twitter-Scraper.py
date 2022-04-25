
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
from ast import Tuple
import csv
from getpass import getpass
from time import sleep

class Scrapper():
    def __init__(self) -> None:
        self.DELAY = 7
    
    
