from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time, datetime

id_company = '0109103532'


def Crawl():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://masothue.com/')
    driver.find_element(By.ID, 'search').send_keys(id_company + Keys.ENTER)
    time.sleep(1)
    name_company = driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/thead').text
    target = driver.find_elements(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr')
    for i in range(1, len(target) - 1):
        print(i)
        td_elements = driver.find_elements(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr[%s]/td' % i)
        label = td_elements[0].text
        value = td_elements[1].text
        print('Label:', label, 'Value:', value)

    time.sleep(10)
    
    driver.close()


if __name__ == "__main__":
    Crawl()
