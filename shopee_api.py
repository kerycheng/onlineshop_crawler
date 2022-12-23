
import requests
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

product_name = '常闇永遠'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(product_name)}'
}

session = requests.Session()
URL = 'https://shopee.tw/api/v4/search/product_labels'
response = session.get(URL, headers=headers)

base_url = 'https://shopee.tw/api/v4/search/search_items/'
query = f'by=relevancy&keyword={product_name}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=29b2d326-776a-4b06-a5be-57b8ae9cfab7'
url = base_url + '?' + query
response = session.get(URL, headers=headers)

print(response.text)

s = Service(r'C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')

driver = webdriver.Chrome(service = s, options = chrome_options)
driver.get(URL)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")

title = soup.find_all("div", class_="ie3A+n bM+7UW Cve6sh")
print(title)
#products = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")

'''
for product in products:
    title = product.find("div", class_="ie3A+n bM+7UW Cve6sh").text
    price = product.find("div", class_="vioxXd rVLWG6").text
    print(title, price)
'''
