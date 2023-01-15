import requests
from bs4 import BeautifulSoup

url = "https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=14&distance=&type=&start=0&_=1673510890038"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("title").get_text()

print(title)