from utils import *
import os

encoding = "utf-8"
output_file = "results.csv"

def search_query(driver, query: str):
    """
    Search For The Given Query
    """
    element = sendkeys(driver, '//input[@id="searchboxinput"]', query)

def main():
    query = "Software Houses in Islamabad"
    url = 'https://www.google.com/maps'

    urlDriver = runDriver()
    urlDriver.get(url)

    search_query(urlDriver, query)

    items_list = getAllElements(urlDriver, '//div[@role="article"]/a[@class="hfpxzc"]')

    for item in items_list:
        item.click()
        time.sleep(1)
        comp_name = item.get_attribute('aria-label')
        print('NAME 1 \t', getElement(urlDriver, '//h1[@class="DUwDvf fontHeadlineLarge"]/span[1]').text)
        print('NAME 2 \t', comp_name)
        print('Address 1 \t', getElement(urlDriver, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]/div[7]/div[3]/button/div/div[2]/div').text)
        # print('Address 2 \t', getElement(urlDriver, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]/div[7]/div[4]/button/div/div[2]/div').text)

if __name__ == "__main__":
    main()