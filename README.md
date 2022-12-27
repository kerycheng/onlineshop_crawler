# 蝦皮爬蟲程式

### 程式介面
![image](https://imgur.com/Lpp3TeI.jpg)

### 程式邏輯圖
![image](https://imgur.com/KZFyE9n.jpg)  
把start.py當作程式進入點，當執行start.py時會進入main_controller.py
main_controller.py會去開啟程式UI介面，之後當我們輸入關鍵字(keyword)、頁數(pages)、檔案儲存路徑(sava_data_path)、選擇要爬取的賣場並按下開始時  
main_comtroller.py獲取以上資料，controller透過檢查賣場按鈕判斷該把資料傳給哪一個scrape.py做處理

### 使用說明
  * 輸入想搜尋的商品關鍵字
  * 輸入想爬取的商品頁數
  * 選擇檔案儲存路徑
  * 點選要爬取資料的賣場(蝦皮、露天)
  * 按下開始按鈕就會開始爬取資料
  
### 目前商品資料類型
  * 僅提供「商品標題」、「最低售價」、「最高售價」以及「已售出數量」
  
### TODO
  * 使用者透過點選想要的資料選項來爬取到需要的資料  
    例：綜合排行or最熱銷  
        只想爬取商品標題、已售出數量、商品評價等
        
### 注意事項
  如果要將程式把包成.exe檔，請輸入以下指令  
  pyinstaller --add-data 'ca.crt;seleniumwire' --add-data 'ca.key;seleniumwire' -i bug.ico -F start.py -w

### 程式參考來源
  * https://www.youtube.com/watch?v=vU-Z9vCsZpQ
  * https://www.youtube.com/watch?v=ohB_o7r4Obo
  * https://ithelp.ithome.com.tw/articles/10274773

### 
  * 2022/12/27 新增檔案儲存路徑、透過state_table顯示程式當前執行狀態、UI界面美化
  * 2022/12/26 新增露天賣場按鈕、加了多執行緒可同時執行兩個賣場爬蟲程序
  * 2022/12/25 新增UI介面、賣場選擇按鈕
  * 2022/12/23 新增蝦皮爬蟲程式
  * 2022/12/22 開始專案
