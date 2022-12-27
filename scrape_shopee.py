import pandas as pd
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.chrome.service import Service as ChromeSerive
from subprocess import CREATE_NO_WINDOW
import json
import time

chrome_service = ChromeSerive('chromedriver')
chrome_service.creation_flags = CREATE_NO_WINDOW
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options, service=chrome_service)

class scrape_shopee(object):
    def __init__(self, keyword, pages, save_path):
        self.keyword = keyword
        self.pages = int(pages)
        self.save_path = save_path

    # 將要抓取的頁面連結存到urls[]裡
    def get_url(self):
        self.urls = []
        if self.pages == 1:
            url = f'https://shopee.tw/search?keyword={self.keyword}&page=0'
            self.urls.append(url)
        else:
            for i in range(0, self.pages - 1): # 蝦皮頁面是從page=0開始算，所以這邊做-1
                url = f'https://shopee.tw/search?keyword={self.keyword}&page={i}'
                self.urls.append(url)

    # 抓取資料
    def scrape(self, url):
        driver.get(url) # 瀏覽器取得網頁連結
        time.sleep(5)
        for request in driver.requests:
            if request.response:
                if request.url.startswith('https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword='): # 若網頁成功跳轉到目標頁面才開始執行
                    response = request.response
                    body = decode(response.body, response.headers.get('Content-Encoding', 'Identity'))
                    decode_body = body.decode('utf8')
                    json_data = json.loads(decode_body) # 將網頁資料全部存進json_data裡

                    data = []
                    rows = json_data['items'] # 總共獲取幾筆資料
                    for i in range(0, len(rows)): # 遍歷每一筆商品
                        product_name = json_data['items'][i]['item_basic']['name'] # 商品標題
                        price_min = str(json_data['items'][i]['item_basic']['price_min'])[:-5] # 商品最低價
                        price_max = str(json_data['items'][i]['item_basic']['price_max'])[:-5] # 商品最高價
                        historical_sold = json_data['items'][i]['item_basic']['historical_sold'] # 已售出

                        data.append(
                            (product_name, price_min, price_max, historical_sold)
                        )
        return data

    # 建一個dataframe將資料存進去
    def data_frame(self, data):
        # '商品標題', '商品最低價', '商品最高價', '已售出'
        self.df = pd.DataFrame(data, columns = ['Product Title', 'Price Min', 'Price Max', 'Historical Sold'])

    # 將抓取到的資料存進excel檔
    def save_to_xlsx(self):
        # excel檔名: Shopee_關鍵字名稱.xlsx
        file_name = f'Shopee_{self.keyword}'
        self.df.to_excel(f'{self.save_path}/{file_name}.xlsx', index = False)

        return f'{file_name}.xlsx'