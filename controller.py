from PyQt5.QtCore import QThread
import threading

from scrape_shopee_controller import scrape_shopee
from scrape_ruten_controller import  scrape_ruten

class controller(QThread):
    def __init__(self, keyword, pages, type):
        self.keyword = keyword
        self.pages = pages
        self.type = type
        self.online_store_type()

    def online_store_type(self):
        if self.type == 'Shopee':
            self.thread_shopee = threading.Thread(target=self.shopee_control)
            self.thread_shopee.start()
        elif self.type == 'Ruten':
            self.thread_ruten = threading.Thread(target=self.ruten_control)
            self.thread_ruten.start()

    def shopee_control(self):
        scrape_shopee(self.keyword, self.pages)

    def ruten_control(self):
        scrape_ruten(self.keyword, self.pages)
