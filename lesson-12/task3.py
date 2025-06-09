import requests
from bs4 import BeautifulSoup
import json
import time

base_url = "https://www.demoblaze.com/"
catalog_url = "https://www.demoblaze.com/index.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

session = requests.Session()
session.headers.update(headers)

def get_laptop_links(soup):
    cards = soup.select('.card-title a')
    return [base_url + card['href'] for card in cards]

def get_laptop_details(url):
    res = session.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    name = soup.find('h2', class_='name').text.strip()
    price = soup.find('h3', class_='price-container').text.strip().split(' ')[0].replace('$', '')
    description = soup.find('div', id='more-information').text.strip()
    return {
        "name": name,
        "price": price,
        "description": description
    }

data = []
current_page = 1

while True:
    page_url = f"https://www.demoblaze.com/index.html"
    res = session.get(page_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    links = get_laptop_links(soup)
    for link in links:
        details = get_laptop_details(link)
        data.append(details)
        time.sleep(1)
    next_button = soup.find("button", id="next2")
    if "disabled" in next_button.get("class", []):
        break
    session.get(base_url + "entries", params={"cat": "notebook", "page": current_page})
    current_page += 1
    time.sleep(1)

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
