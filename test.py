from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver_path = 'C:/Users/hasib/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(driver_path)

# navigate to the product details page
product_url = 'https://shop.adidas.jp/products/EG4958'
driver.get(product_url)

# wait for the reviews to load
reviews_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'BVRRDisplayContentID'))
)

# extract the reviews
reviews = reviews_container.find_elements_by_class_name('BVRRReviewDisplayStyle5')

# loop through the reviews and extract the information
for review in reviews:
    date = review.find_element_by_class_name('BVRRReviewDate').text.strip()
    rating = review.find_element_by_class_name('BVRRRatingNormalImage > img').text.strip()
    title = review.find_element_by_class_name('BVRRReviewTitle').text.strip()
    description = review.find_element_by_class_name('BVRRReviewText').text.strip()
    user_id = review.find_element_by_class_name('BVRRNickname').text.strip()
    print(date, rating, title, description, user_id)

# close the browser
driver.quit()
