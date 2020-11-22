#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Date:2020-10
#Author:wjt
#description: 爬虫公共方法

import requests
from bs4 import BeautifulSoup

import json
import time

from fake_useragent import UserAgent  # 爬虫请求头伪装
# 导入 random(随机数) 模块
import random

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)  # 禁止https(ssl)问题的警告

def get_url(my_url):
    """
    请求网站公共方法
    """
    
    ua = UserAgent()  # 爬虫请求头伪装

    # 定制请求头
    my_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ASPSESSIONIDSQSTBQTS=JHFBIOABFFJKOCKGPMICDOAD; UM_distinctid=175abc65cd4466-0c25d9296651e6-75143d4c-13c680-175abc65cd536d; CNZZDATA76666=cnzz_eid%3D1125814118-1604900918-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1604900918; __gads=ID=0eefa12aff88b511-228530daa7c40003:T=1604904705:RT=1604904705:S=ALNI_MYjs_NMmvBy6bl1Xc_mfcMyMWnNhQ',
        # 'Host': 'www.876543.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.chrome,
    }

    r = requests.get(url=my_url,  headers=my_headers, timeout=5,  verify=False)
    r.encoding = r.apparent_encoding
    if r.status_code==200:
        return r.text
