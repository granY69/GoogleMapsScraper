from utils import *
import os

def search_query(driver, query: str):
    """
    Search For The Given Query
    """
    url = driver.current_url
    element = sendkeys(driver, '//input[@id="searchboxinput"]', query)
    while url == driver.current_url:
        time.sleep(3)
    
def get_items(urlDriver):
    elements = getAllElements(urlDriver, '//div[@role="article"]/a[@class="hfpxzc"]')
    if not elements:
        urlDriver.refresh()
        time.sleep(10)
        elements = getAllElements(urlDriver, '//div[@role="article"]/a[@class="hfpxzc"]')
    if elements:
        return elements
    else:
        print("Check your Internet Connection and Try Again")
        urlDriver.quit()
        return None

def main():
    query = "Software Houses in Blue Area Islamabad"
    url = 'https://www.google.com/maps'

    urlDriver = runDriver()
    urlDriver.get(url)

    search_query(urlDriver, query)

    # os.system('pause')

    comp_names_list = get_items(urlDriver)
    if comp_names_list:
        data = {
            "Name": [],
            "Address": [],
            "Website": [],
            "Contact_No": []
        }
        total = len(comp_names_list)
        count = 0
        for item in comp_names_list:
            print(f"Iteration no {count+1}/{total}")
            c_name = item.get_attribute('aria-label')
            item.click()
            element = getElement(urlDriver, f'//h1[@class="DUwDvf fontHeadlineLarge"]/span[contains(text(), "{c_name}")]')
            if element:
                name = element.text
            else:
                name = False
            element = getElement(urlDriver, f'//div[@role="main" and @aria-label="{c_name}"][1]/div[2]/div[7]/div[3]/button/div/div[2]/div')
            if element:
                address = element.text
            else:
                address = False

            element = getElement(urlDriver, f'//div[@role="main" and @aria-label="{c_name}"][1]/div[2]/div[7]/div/a[@data-tooltip]')
            if element:
                website = element.get_attribute('href')
            else:
                website = "NOT FOUND"

            element = getElement(urlDriver, f'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png"]/../../../div[2]/div')
            if not element:
                element = getElement(urlDriver, f'//img[@src="//www.gstatic.com/images/icons/material/system_gm/2x/phone_gm_blue_24dp.png"]/../../../div[2]/div')
            if element:
                phone = element.text
            else:
                phone = "NOT FOUND"

            data["Name"].append(name)
            data["Address"].append(address)
            data["Website"].append(website)
            data["Contact_No"].append(phone)
            count+=1
        pd.DataFrame(data).to_csv('result.csv', index=False)
        urlDriver.quit()
    else:
        return "Program Stopped Error Occured"

if __name__ == "__main__":
    main()