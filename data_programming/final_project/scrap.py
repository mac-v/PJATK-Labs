from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import pandas as pd
from io import StringIO


def get_page(url):
    service = Service("/snap/bin/geckodriver")
    d = webdriver.Firefox(service=service)
    d.get(url)
    return d


def click_accept_consent_button(driver):
    button_consent = driver.find_element(By.CLASS_NAME, "fc-cta-consent")
    button_consent.click()


def transform_date(df):
    months = {"sty": "Jan", "lut": "Feb", "mar": "Mar", "kwi": "Apr", "maj": "May", "cze": "Jun",
              "lip": "Jul", "sie": "Aug", "wrz": "Sep", "paź": "Oct", "lis": "Nov", "gru": "Dec"}

    df[2] = df[2].map(months)
    df[3] = df[3].astype(str)
    df[1] = df[1].astype(str)
    df[11] = pd.to_datetime(df[[3, 2, 1]].agg(' '.join, axis=1), format='%Y %b %d')
    df = df.drop(columns=[1, 2, 3])

    return df


def get_table_data(d):
    table = d.find_element(By.CLASS_NAME, "fth1")
    table_body = table.find_element(By.TAG_NAME, "tbody")
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    df = pd.DataFrame()

    for row in table_rows:
        df_row = pd.read_csv(StringIO(row.text), sep=" ", header=None)
        df_row = transform_date(df_row)
        df = pd.concat([df, df_row])
    return df


def count_pages(d):
    page_nav = d.find_element(By.XPATH, "//tr[@id='r']/td[@id='f13']")
    children = page_nav.find_elements(By.TAG_NAME, "a")
    return children[-1].get_attribute("href").split("=")[-1]


def scrape_data():
    base_url = "https://stooq.pl/q/d/?s=es.c&i=d"
    d = get_page(base_url)
    click_accept_consent_button(d)
    time.sleep(3)
    max_pages = count_pages(d)
    print(max_pages)

    df = pd.DataFrame()
    for page in range(1, max_pages+1):
        url_with_pagination = f"https://stooq.pl/q/d/?s=es.c&i=d&l={page}"
        d.get(url_with_pagination)
        df = pd.concat([df, get_table_data(d)])
    d.quit()
    return df

