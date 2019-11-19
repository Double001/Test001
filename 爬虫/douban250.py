#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- author:Double -*-

import requests
from bs4 import BeautifulSoup       #导入BTS

class Douban:

    def __init__(self):
        self.URL = 'https://movie.douban.com/top250'    #需要爬取的网页URL
        self.startnum = []                              #定义数组存放页码
        for start_num in range(0,251,25):               #页码范围以及取值
            self.startnum.append(start_num)
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
            # Header相当于伪装，即通过该身份id获取列表信息
    def get_top250(self):
        for start in self.startnum:
            start = str(start)                          #转换start格式为字符串
            html = requests.get(self.URL, params={'start':start})           #键值对
            soup = BeautifulSoup(html.text,"html.parser")
            name = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span')
            for name in name:
                print(name.get_text())



if __name__ == "__main__":
    cls = Douban()
    cls.get_top250()