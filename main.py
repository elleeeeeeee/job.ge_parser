from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from job import Job
from db import DataBase
import time

url = "https://jobs.ge/?page=1&q=&cid=6&lid=&jid="
response = requests.get(url)
soap = BeautifulSoup(response.content, "html.parser")
num = soap.find("table", {"id": "job_list_table"})

soap_2 = BeautifulSoup(str(num), 'html.parser')
trs = soap_2.find_all('tr')


driver = webdriver.Chrome()
i = 2

while i != len(trs):
    driver.get("https://jobs.ge/?page=1&q=&cid=6&lid=&jid=")
    title = driver.find_element(By.XPATH, f'//*[@id="job_list_table"]/tbody/tr[{i}]/td[2]/a[1]')
    title.click()

    name = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/b').text

    description = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[4]/td').text

    description_lst = description.split()
    for e in range(len(description_lst)):
        if description_lst[e-1].isnumeric() and "ლარ" in description_lst[e] or "gel" in description_lst[e] or "GEL" in description_lst[e]:
            salary = description_lst[e-1]
            break
        else:
            salary = None

    company = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[2]/td/b').text

    start_date = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[1]').text

    deadline = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[2]').text

    for a in description_lst:
        if "@" in a:
            email = a
        else:
            email = None
    i += 1

    line = Job(name, description, company, start_date, deadline, salary, email)
    d_base = DataBase("job.db")
    d_base.add(line)


