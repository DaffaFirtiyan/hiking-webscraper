import requests
from bs4 import BeautifulSoup

url = "https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=14&distance=&type=&start=0&_=1673510890038"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# write the prettified html to a text file
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# extract the title of the web page
title = soup.find("title").get_text()

# write the title to the text file
with open("output.txt", "a") as file:
    file.write(title)