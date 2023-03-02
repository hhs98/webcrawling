import csv
import requests
from bs4 import BeautifulSoup

# with open("product_links.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     product_links = [row[0] for row in reader]

product_data = []

url = "https://shop.adidas.jp/products/EG4958"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

# Get the product name
product_name = soup.select_one("h1.itemTitle").text.strip()

# Get the product category
product_category = soup.select_one("li.breadcrumbListItem:nth-child(4) > a").text.strip()

# Get the image URL
# image_url = soup.select_one("img.magnify_image_wrapper").get("src")

# get all the image urls
image_urls = ", ".join(["https://shop.adidas.jp" + img.get("src") for img in soup.select("img.test-main_image")])

# Get the description header and description
description_header = soup.select_one("h2.test-commentItem-topHeading").text.strip()
description = soup.select_one("div.commentItem-mainText").text.strip()

sizes = ", ".join([bt.text.strip() for bt in soup.select("ul.sizeSelectorList > li > button")])



# user_reviews = []
# review_items = soup.select("div.BVRRReviewDisplayStyle5")
# for item in review_items:
#     date = item.select_one("span.BVRRReviewDate").text.strip()
#     rating = item.select_one("div.BVRRRatingNormalImage > img")["title"].strip()
#     review = item.select_one("span.BVRRReviewText").text.strip()
#     title = item.select_one("span.BVRRReviewTitle").text.strip()
#     user_id = item.select_one("span.BVRRNickname").text.strip()
#     user_reviews.append({
#         "date": date,
#         "rating": rating,
#         "review": review,
#         "title": title,
#         "user_id": user_id
#     })


# Get the tags
tags = ", ".join([tag.text.strip() for tag in soup.select("div.itemTagsPosition > div > div > a")])


# Add the scraped data to the list
product_data.append({
    "name": product_name,
    "category": product_category,
    "images": image_urls,
    "description_title": description_header,
    "description": description,
    "sizes": sizes,
    "user_reviews": [],
    "keywords": tags
})

# Save the scraped data to a CSV file
with open("adidas_products.csv", "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["name", "category", "images", "description_title", "description", "sizes", "user_reviews", "keywords"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for product in product_data:
        writer.writerow(product)
