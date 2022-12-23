# 蝦皮爬蟲程式

### 使用說明
  * 輸入想搜尋的商品關鍵字
  * 輸入想爬取的商品頁數
  
### 目前程式功能
  * 僅提供「商品標題」、「最低售價」、「最高售價」以及「已售出數量」
  
### TODO
  * 增加GUI介面
  * 使用者透過點選想要的資料選項來爬取道需要的資料  
    例：綜合排行or最熱銷  
        只想爬取商品標題、已售出數量、商品評價等
        
### 注意事項
  如果要將程式把包成.exe檔，請輸入以下指令  
  pyinstaller --add-data 'ca.crt;seleniumwire' --add-data 'ca.key;seleniumwire' --onefile scrape_shopee.py
        
### 程式參考來源
  * https://www.youtube.com/watch?v=vU-Z9vCsZpQ
  * https://www.youtube.com/watch?v=ohB_o7r4Obo&t=423s
