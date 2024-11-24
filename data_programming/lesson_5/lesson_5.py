## Task 1.
# User-agent: *
# # Directories
# Disallow: /wyszukiwanie/
# Disallow: /en/search/
# Disallow: /core/
# Disallow: /profiles/
# Disallow: /node/
# Disallow: /en/node/
# Disallow: /ru/node/
# Disallow: /ua/node/
# # Files
# Disallow: /README.txt
# Disallow: /web.config
# # Paths (clean URLs)e
# Disallow: /admin/
# Disallow: /comment/
# Disallow: /filter/
# Disallow: /search/
# Disallow: /user/
# Disallow: /media/oembed
# Disallow: /*/media/oembed
# Disallow: /index.php/

## Answers 1.
# 1. User-agent: * → asterisk sign, meaning all user agents must or should obey the rules below

# 2. Directories (Disallow): URL Paths and their child paths
# (that have directory at the start) that are disallowed from searching

# 3. Files (disallow): Files that are disallowed from searching

# 4. Paths (clean URLs): URL paths that are disallowed from searching


## Task 2.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import requests

class Scrapper():

    def __init__(self, path_to_images):
        self.driver = self.init_driver()
        self.accept_cookies()
        self.maximize_window()
        self.change_language()
        self.go_to_business()
        titles = self.get_titles()
        print(titles)
        self.save_images(path_to_images)
        self.scroll_down_page()
        max_page = self.get_last_page()
        print("Max page: ", max_page)

    def init_driver(self):
        download_service = Service()
        driver = webdriver.Chrome(service=download_service)
        driver.get(r"https://www.pap.pl/")
        return driver

    def accept_cookies(self):
        btn_agree = self.driver.find_element(By.CLASS_NAME, 'closeButton')
        btn_agree.click()

    def maximize_window(self):
        self.driver.maximize_window()

    def change_language(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        dropdown.click()
        link_eng = self.driver.find_element(By.CLASS_NAME, "choice-en")
        link_eng.click()

    def go_to_business(self):
        link = self.driver.find_element(By.XPATH, '//a[@href="/en/business"]')
        link.click()

    def get_titles(self):
        titles = self.driver.find_elements(By.CLASS_NAME, "title")
        return [title.text for title in titles]

    def save_images(self, path_to_img):
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        os.makedirs(path_to_img, exist_ok=True)
        for i, image in enumerate(images):
            src = image.get_property("src")
            response = requests.get(src)
            if response.status_code == 200:
                image_path = os.path.join(path_to_img, f"image_{i + 1}.jpg")
                with open(image_path, "wb") as f:
                    f.write(response.content)
                print(f"Saved: {image_path}")
            else:
                print(f"Failed: {src}")

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_last_page(self):
        max_page = self.driver.find_element(By.XPATH, "//a[@title='Go to last page']")
        href = max_page.get_attribute("href")
        page_number = href.split("page=")[-1]
        return page_number

s = Scrapper("images")
