import requests
from bs4 import BeautifulSoup

url = "https://www.trademe.co.nz/a/property/residential/rent/search?suburb=967&suburb=1538&suburb=1560&suburb=2638&bedrooms_min=3&sort_order=priceasc"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", class_=["tm-property-search-container","ng-star-inserted"])
houses = results.find_all("div", class_="tm-property-search-card__details")
print(results.prettify())

# for house in results:
#     address = house.find("tm-property-search-card-listing-title", id="1675308589746-3835683851-standard-search-card-title")
#     price = house.find("div", class_="tm-property-search-card-price-attribute__price")
#     if address and price:
#         print(f"Address: {address.text.strip()}")
#         print(f"Price: {price.text.strip()}")
#         print()
#     else:
#         print("did not find any")
#         count = count+1

# print(count)