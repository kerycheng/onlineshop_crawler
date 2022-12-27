from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
import threading
import icon

from scrape_ui import Ui_MainWindow
from scrape_shopee import scrape_shopee
from scrape_ruten import scrape_ruten

class controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def initUI(self):
        self.setWindowIcon(QIcon(':/bug.ico'))

    def setup_control(self):
        self.ui.start_button.clicked.connect(self.onButtonClick)
        self.ui.save_path_button.clicked.connect(self.save_data_path)

    def save_data_path(self):
        self.directory = QFileDialog.getExistingDirectory(None, "選擇儲存資料夾", "c:/")
        self.ui.save_path_input.setText(self.directory)

    def onButtonClick(self): # 按下開始按鈕
        self.product_keyword = self.ui.keyword_input.text() # 獲取商品關鍵字
        self.product_pages = self.ui.pages_input.text() # 獲取要爬取的頁數

        if self.ui.type_shopee_button.isChecked(): # 按下shopee按鈕
            self.display_text('開始執行蝦皮爬蟲')
            self.thread_scrape_shopee = threading.Thread(target=self.shopee_control)
            self.thread_scrape_shopee.start()

        if self.ui.type_ruten_button.isChecked(): # 按下ruten按鈕
            self.display_text('開始執行露天爬蟲')
            self.thread_scrape_ruten = threading.Thread(target=self.ruten_control)
            self.thread_scrape_ruten.start()

    def display_text(self, text): # 把接收到的text文字顯示在state_table(textBrowser)上
        self.ui.state_table.append(f'{text}')

    def shopee_control(self): # 執行scrape_shopee
        self.scrape_shopee = scrape_shopee(self.product_keyword, self.product_pages, self.directory)

        self.display_text('獲取商品關鍵字連結')
        self.scrape_shopee.get_url() # 獲取所要爬的關鍵字連結

        self.display_text('獲取商品資訊')
        dt_all = [] # 用來存取商品資訊
        for i in range(0, len(self.scrape_shopee.urls)):
            scrapes = self.scrape_shopee.scrape(self.scrape_shopee.urls[i])
            dt_all.extend(scrapes)

        self.display_text('建立商品資訊表格')
        self.scrape_shopee.data_frame(dt_all) # 建一個dataframe

        dataframe_name = self.scrape_shopee.save_to_xlsx() # 把dataframe存成excel檔
        self.display_text(f'儲存完畢，檔案名稱為"{dataframe_name}"')

    def ruten_control(self): # 執行scrape_ruten
        self.scrape_ruten = scrape_ruten(self.product_keyword, self.product_pages, self.directory)

        self.display_text('獲取商品關鍵字連結')
        self.scrape_ruten.get_url() # 獲取所要爬的關鍵字連結

        self.display_text('獲取商品資訊')
        dt_all = [] # 用來存取商品資訊
        for i in range(0, len(self.scrape_ruten.urls)):
            scrapes = self.scrape_ruten.scrape(self.scrape_ruten.urls[i])
            dt_all.extend(scrapes)

        self.display_text('建立商品資訊表格')
        self.scrape_ruten.data_frame(dt_all) # 建一個dataframe

        dataframe_name = self.scrape_ruten.save_to_xlsx() # 把dataframe存成excel檔
        self.display_text(f'儲存完畢，檔案名稱為"{dataframe_name}"')
