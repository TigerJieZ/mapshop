import requests
import re
import threading
import time
import pickle
from fake_useragent import UserAgent
import numpy as np
from utils.tools import *
import logging
import os
import time
import json


class SpyderBaidu:
    def __init__(self):
        self.threads_city = []
        self.threads_key = []
        self.key_list = []
        self.city_list = []

        self.SLEEP_TIME = 0.1

        self.city_codes = pickle.load(open('data/city_code.pkl', 'rb'))

        # self.ua = UserAgent()

        self.url = 'http://map.baidu.com/'

        self.shop_list = []

        # 第一步，创建一个logger
        self.logger = logging.getLogger()
        self.init_log()

    def init_log(self):
        self.logger.setLevel(logging.INFO)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname('log/')
        log_name = log_path+'/' + rq + '.log'
        print(log_name)
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        self.logger.addHandler(fh)

    def __str__(self):
        return '基于百度地图的店铺信息爬取器'

    def run(self, city_list, key_list, thread=None):
        """
        抓取指定城市&关键词的店铺信息
        :param city_list: 城市列表
        :param key_list: 关键词列表
        :return:
        """

        self.logger.info('>>>>>>>>>>开始抓取店铺信息>>>>>>>>>>')

        self.key_list = key_list
        self.city_list = city_list
        self.logger.info('城市列表：' + str(self.city_list))
        self.logger.info('行业词列表：' + str(self.key_list))

        def process_key(_key, _city_list):
            for city in _city_list:
                for i in range(0, 100):
                    form_data = self.format_parameter(city, _key, i)

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87Safari/537.36'}

                    htm = requests.get(self.url, params=form_data, headers=headers)
                    htm = htm.text.encode('latin-1').decode('unicode_escape')  # 转码
                    pattern = r'(?<=\baddress_norm":"\[).+?(?="ty":)'
                    htm = re.findall(pattern, htm)  # 按段落匹配

                    for r in htm:
                        pattern = r'(?<=\b"\},"name":").+?(?=")'
                        name = re.findall(pattern, r)
                        if not name:
                            pattern = r'(?<=\b,"name":").+?(?=")'
                            name = re.findall(pattern, r)
                        # print(name[0]) # 名称

                        pattern = r'.+?(?=")'
                        adr = re.findall(pattern, r)
                        pattern = r'\(.+?\['
                        address = re.sub(pattern, ' ', adr[0])
                        pattern = r'\(.+?\]'
                        address = re.sub(pattern, ' ', address)
                        # print(address) # 地址

                        pattern = r'(?<="phone":").+?(?=")'
                        phone = re.findall(pattern, r)
                        try:
                            if phone[0] and '",' != phone[0]:
                                phone_list = phone[0].split(sep=',')
                                for number in phone_list:
                                    if re.match('1', number):
                                        shop = {'name': name[0], 'address': strlist_join(address.split(' ')[2:]),
                                                'quyu': address.split(' ')[1],
                                                'tel': number, 'key': _key}
                                        print(address + ',' + number)
                                        self.shop_list.append(shop)
                                        if thread is not None:
                                            thread.trigger.emit()
                        except Exception as e:
                            print(e)
                            pass

        while self.threads_key or self.key_list:
            # the crawl is still active
            for thread in self.threads_key:
                if not thread.is_alive():
                    # remove the stopped threads
                    self.threads_key.remove(thread)
            while len(self.threads_key) < 20 and self.key_list:
                key = self.key_list.pop()
                thread = threading.Thread(target=process_key(key, city_list))
                thread.setDaemon(True)
                thread.start()
                self.threads_key.append(thread)
            time.sleep(self.SLEEP_TIME)

    def format_parameter(self, city, key, pageno):
        """
        格式化查询店铺所需提交的表单
        :param city: 城市名
        :param key:
        :param pageno:
        :return:
        """
        city_code = self.get_city_code(city)

        parameter = {
            "newmap": "1",
            "reqflag": "pcmap",
            "biz": "1",
            "from": "webmap",
            "da_par": "direct",
            "pcevaname": "pc4.1",
            "qt": "con",
            "c": city_code,  # 城市代码
            "wd": key,  # 搜索关键词
            "wd2": "",
            "pn": pageno,  # 页数
            "nn": pageno * 10,
            "db": "0",
            "sug": "0",
            "addr": "0",
            "da_src": "pcmappg.poi.page",
            "on_gel": "1",
            "src": "7",
            "gr": "3",
            "l": "12",
            "tn": "B_NORMAL_MAP",
            # "u_loc": "12621219.536556,2630747.285024",
            "ie": "utf-8",
            # "b": "(11845157.18,3047692.2;11922085.18,3073932.2)", #这个应该是地理位置坐标，可以忽略
            "t": "1468896652886"}
        return parameter

    def get_city_code(self, city_str):
        """
        获取city对应的code
        :param city_str:
        :return:
        """
        for city_code in self.city_codes:
            if city_code['name'] == city_str:
                return city_code['code']


if __name__ == '__main__':
    spyder = SpyderBaidu()
    spyder.run(['上海市'], ['网吧', '筛网'])
    print(spyder.shop_list)
