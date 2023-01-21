from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

url_easy = "https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=14&distance=&type=&start=0&_=1673510890038"
url_intermediate = "https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=15&distance=&type=&start=0&_=1674344874509"

driver = webdriver.ChromiumEdge()
driver.get(url_intermediate)
wait = WebDriverWait(driver, 30)
element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "el-panel__block")))
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

results = soup.find("div", class_=["results", "results--ofsearch"])
trails = results.find_all("div", class_=["el-panel__block", "el-panel__block--25", "pure-u-16-16", "pure-u-sm-12-24", "pure-u-lg-6-24"])

# print(len(trails))
with open("trails_intermediate.csv","w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Location", "Distance"])
    for trail in trails:
        name = trail.find("div", class_="el-teaser__title")
        loc = trail.find("div", class_="info--location").find("span", class_="info__text")
        dist = trail.find("div", class_="info--distance").find("span", class_="info__text")
        writer.writerow([name.text.strip(), loc.text.strip(), dist.text.strip()])
driver.quit()