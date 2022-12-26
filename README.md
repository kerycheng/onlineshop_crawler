# 蝦皮爬蟲程式

### 程式介面
![image](https://imgur.com/Krc77wV.jpg)

### 程式邏輯圖
![image](https://imgur.com/DhBsT6I.jpg)  
透過輸入關鍵字(keyword)和頁數(pages)，並按下想爬取的賣場按鈕(online store type)  
UI將資料傳給controller，controller透過賣場類別判斷該把資料傳給哪一個scrape.py做處理  

### 使用說明
  * 輸入想搜尋的商品關鍵字
  * 輸入想爬取的商品頁數
  * 點選要爬取資料的賣場(蝦皮、露天)
  
### 目前程式功能
  * 僅提供「商品標題」、「最低售價」、「最高售價」以及「已售出數量」
  
### TODO
  * 透過UI的state_table顯示scrape當前執行到哪個階段
  * 使用者透過點選想要的資料選項來爬取到需要的資料  
    例：綜合排行or最熱銷  
        只想爬取商品標題、已售出數量、商品評價等
        
### 注意事項
  如果要將程式把包成.exe檔，請輸入以下指令  
  pyinstaller --add-data 'ca.crt;seleniumwire' --add-data 'ca.key;seleniumwire' --onefile scrape_ui.py --noconsole
        
### 程式參考來源
  * https://www.youtube.com/watch?v=vU-Z9vCsZpQ
  * https://www.youtube.com/watch?v=ohB_o7r4Obo&t=423s


### 
  * 2022/12/26 新增露天賣場按鈕、加了多執行續可同時執行兩個賣場爬蟲程序
  * 2022/12/25 新增UI介面、賣場選擇按鈕
  * 2022/12/23 新增蝦皮爬蟲程式
  * 2022/12/22 開始專案
