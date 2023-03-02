import requests
from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(requests.get("https://shop.adidas.jp/men").content, "html.parser")


item_links = []
for item in soup.find_all("a", href=lambda href: href and href.startswith("/item/?gender=mens")):
    item_links.append(item["href"])

item_links = list(set(item_links))

product_links = []

for link in item_links:
    soup = BeautifulSoup(requests.get("https://shop.adidas.jp" + link).content, "html.parser")
    for product in soup.select("a.image_link.test-image_link"):
        product_links.append(product["href"])

    product_links = list(set(product_links))
    if len(product_links) >= 300:
        break
  

with open("product_links.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for link in product_links:
        writer.writerow([link])
