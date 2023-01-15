import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("title").get_text()
results = soup.find(id="ResultsContainer")

jobElements = results.find_all("div", class_="card-content")

for jobElement in jobElements:
    title = jobElement.find("h2", class_="title")
    comp = jobElement.find("h3", class_="company")
    loc = jobElement.find("p", class_="location")
    # print(title.text.strip())
    # print(comp.text.strip())
    # print(loc.text.strip())
    # print()

pythonJobs = results.find_all("h2", string=lambda text: "python" in text.lower())

pythonJobsElements = [h2_element.parent.parent.parent for h2_element in pythonJobs]

for jobElement in pythonJobsElements:
    title = jobElement.find("h2", class_="title")
    comp = jobElement.find("h3", class_="company")
    loc = jobElement.find("p", class_="location")
    print(title.text.strip())
    print(comp.text.strip())
    print(loc.text.strip())

    links = jobElement.find_all("a")
    for link in links:
        linkURL = jobElement.find_all("a")[1]["href"]
        print(f"Apply here: {linkURL}\n")

    print()

# print(title)
# print(jobElement.prettify())
# print(soup.prettify())