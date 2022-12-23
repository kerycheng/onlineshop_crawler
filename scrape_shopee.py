import sys
import pandas as pd
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

keyword = input('請輸入商品關鍵字: ')
pages = int(input('請輸入要抓取的頁數: '))

# 將要抓取的頁面連結存到urls[]裡
def get_url(keyword, pages):
    print('獲取商品關鍵字網頁連結中')
    urls = []
    if pages == 1:
        url = f'https://shopee.tw/search?keyword={keyword}&page=0'
        urls.append(url)
    else:
        for i in range(0, pages - 1): # 蝦皮頁面是從page=0開始算，所以這邊做-1
            url = f'https://shopee.tw/search?keyword={keyword}&page={i}'
            urls.append(url)
    return urls

# 抓取資料
def scrape(url):
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
def data_frame(data):
    print('建立資料表格')
    # '商品標題', '商品最低價', '商品最高價', '已售出'
    df = pd.DataFrame(data, columns = ['Product Title', 'Price Min', 'Price Max', 'Historical Sold'])
    return df

# 將抓取到的資料存進excel檔
def save_to_xlsx(df, keyword):
    # excel檔名: Shopee_關鍵字名稱.xlsx
    file_name = f'Shopee_{keyword}'
    df.to_excel(f'{file_name}.xlsx', index = False)
    print(f'儲存完畢，檔案名稱為"{file_name}.xlsx"')

if __name__ == '__main__':
    urls = get_url(keyword, pages) # 獲取所要爬的關鍵字連結
    dt_all = [] # 用來存取商品資訊
    for i in range(0, len(urls)):
        scrapes = scrape(urls[i])
        dt_all.extend(scrapes)

    dt_frame = data_frame(dt_all) # 建一個dataframe
    save_to_xlsx(dt_frame, keyword) # 把dataframe存成excel檔
    sys.exit()  # 結束程式
