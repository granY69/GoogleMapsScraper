import pandas as pd
import time
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime

timeout = 10

def runDriver():
    """
    Creates an instance of webdriver chrome
    """
    options = Options()
    # options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    # options.add_argument('headless')
    # options.add_argument("--blink-settings=imagesEnabled=false")
    return webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

def click(driver, xpath : str):
    """
    Finds the element and perform click operation
    """
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def getElement(driver, xpath : str):
    """
    find element and return its object
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

def getAllElements(driver, xpath : str):
    """
    find all elements and return its object
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

def sendkeys(driver, xpath : str, keys : str):
    """
    Finds the element and send keys
    """
    getElement(driver, xpath).send_keys(keys)
    getElement(driver, xpath).send_keys(Keys.RETURN)