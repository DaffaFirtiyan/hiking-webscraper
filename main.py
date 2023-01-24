import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

url_easy = "https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=14&distance=&type=&start=0&_=1673510890038"

driver = webdriver.ChromiumEdge()
driver.get(url_easy)
wait = WebDriverWait(driver, 60)

counter = 0

for i in range(4):
    try:
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button--more")))
        if button.is_displayed():
            driver.execute_script("arguments[0].click();", button)
            time.sleep(5)  # Add a small delay to allow the page to load after the button click
            counter += 1
    except NoSuchElementException:
        break

if counter == 4:
    element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "el-panel__block")))
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    results = soup.find("div", class_=["results", "results--ofsearch"])
    trails = results.find_all("div", class_=["el-panel__block", "el-panel__block--25", "pure-u-16-16", "pure-u-sm-12-24", "pure-u-lg-6-24"])

    # print(len(trails))
    with open("trails.csv","w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Location", "Distance"])
        for trail in trails:
            name = trail.find("div", class_="el-teaser__title")
            loc = trail.find("div", class_="info--location").find("span", class_="info__text")
            dist = trail.find("div", class_="info--distance").find("span", class_="info__text")
            writer.writerow([name.text.strip(), loc.text.strip(), dist.text.strip()])

    try:
        driver.quit()
    except:
        driver.close()

    print("finished :)")