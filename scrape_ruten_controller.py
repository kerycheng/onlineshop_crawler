import pandas as pd
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.chrome.service import Service as ChromeSerive
from subprocess import CREATE_NO_WINDOW
import json
import time

from scrape_ui import Ui_MainWindow
chrome_service = ChromeSerive('chromedriver')
chrome_service.creation_flags = CREATE_NO_WINDOW
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options, service=chrome_service)

class scrape_ruten(object):
    def __init__(self, keyword, pages):
        self.keyword = keyword
        self.pages = int(pages)

        self.get_url() # 獲取所要爬的關鍵字連結
        dt_all = [] # 用來存取商品資訊
        for i in range(0, len(self.urls)):
            scrapes = self.scrape(self.urls[i])
            dt_all.extend(scrapes)

        self.data_frame(dt_all) # 建一個dataframe
        self.save_to_xlsx() # 把dataframe存成excel檔

    # 將要抓取的頁面連結存到urls[]裡
    def get_url(self):
        print('獲取商品關鍵字網頁連結中')
        self.urls = []
        for i in range(0, self.pages):
            url = f'https://www.ruten.com.tw/find/?q={self.keyword}&p={i+1}'
            self.urls.append(url)

    # 抓取資料
    def scrape(self, url):
        driver.get(url) # 瀏覽器取得網頁連結
        time.sleep(5)
        for request in driver.requests:
            if request.response:
                if request.url.startswith('https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod?id='): # 若網頁成功跳轉到目標頁面才開始執行
                    response = request.response
                    body = decode(response.body, response.headers.get('Content-Encoding', 'Identity'))
                    decode_body = body.decode('utf8')
                    json_data = json.loads(decode_body) # 將網頁資料全部存進json_data裡

                    data = []
                    rows = json_data # 總共獲取幾筆資料
                    for i in range(0, len(rows)): # 遍歷每一筆商品
                        product_name = json_data[i]['ProdName'] # 商品標題
                        price_min = json_data[i]['PriceRange'][0] # 商品最低價
                        price_max = json_data[i]['PriceRange'][1] # 商品最高價
                        historical_sold = json_data[i]['SoldQty'] # 已售出

                        data.append(
                            (product_name, price_min, price_max, historical_sold)
                        )
        return data

    # 建一個dataframe將資料存進去
    def data_frame(self, data):
        print('建立資料表格')
        # '商品標題', '商品最低價', '商品最高價', '已售出'
        self.df = pd.DataFrame(data, columns = ['Product Title', 'Price Min', 'Price Max', 'Historical Sold'])

    # 將抓取到的資料存進excel檔
    def save_to_xlsx(self):
        # excel檔名: Shopee_關鍵字名稱.xlsx
        file_name = f'Ruten_{self.keyword}'
        self.df.to_excel(f'{file_name}.xlsx', index = False)
        print(f'儲存完畢，檔案名稱為"{file_name}.xlsx"')