from scrape_shopee_controller import scrape_shopee

class controller(object):
    def __init__(self, keyword, pages, type):
        self.keyword = keyword
        self.pages = pages
        self.type = type
        self.online_store_type()

    def online_store_type(self):
        if self.type == 'Shopee':
            self.shopee_control()
        elif self.type == 'Ruten':
            print('此功能尚未開放')

    def shopee_control(self):
        scrape_shopee(self.keyword, self.pages)
        '''
        self.urls = scrape_shopee.get_url() # 獲取所要爬的關鍵字連結
        dt_all = [] # 用來存取商品資訊
        for i in range(0, len(self.urls)):
            scrapes = scrape_shopee.scrape(self.urls[i])
            dt_all.extend(scrapes)

        scrape_shopee.data_frame(dt_all) # 建一個dataframe
        scrape_shopee.save_to_xlsx() # 把dataframe存成excel檔
        '''