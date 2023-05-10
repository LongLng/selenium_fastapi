from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time, datetime


class MyParam(BaseModel):
    mst: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/submit")
async def submit(item: MyParam):
    res = {}
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://masothue.com/')
    # print(item.id_company)
    driver.find_element(By.ID, 'search').send_keys(str(item.mst) + Keys.ENTER)
    time.sleep(1)
    name_company = driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/thead').text
    if name_company is None:
        return {
            "Error": "invalid_number",
            "Message": "MA SO THUE KHONG HOP LE"
        }
    res.update({
        "name_company": name_company,
    })
    target = driver.find_elements(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr')
    for i in range(1, len(target) - 1):
        print(i)
        td_elements = driver.find_elements(By.XPATH, '//*[@id="main"]/section[1]/div/table[1]/tbody/tr[%s]/td' % i)
        label = td_elements[0].text
        value = td_elements[1].text
        value_data = {
            label: value
        }
        res.update(value_data)
        print('Label:', label, 'Value:', value)

    driver.close()
    return res
