from requests_html import HTMLSession

session = HTMLSession()

query = input("place: ").capitalize()
url = f"https://www.google.com/search?q=weather+{query}"

req = session.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"})

temperature = req.html.find("span#wob_tm", first = True).text
unit = req.html.find("div.vk_bk.wob-unit span.wob_t", first = True).text
desc = req.html.find("div.VQF4g", first = True).find("span#wob_dc", first = True).text

print(query, temperature, unit, desc)