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
from requests_toolbelt import MultipartEncoder

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

def itellyou_post(father_key,url):
    """
    我告诉你 pos方法获取目录
    """
    ua = UserAgent()  # 爬虫请求头伪装
    
    payload = {'id': father_key}
    m = MultipartEncoder(payload)
    # 定制请求头
    my_headers = {
        # ':authority': 'msdn.itellyou.cn',
        # ':method': 'POST',
        # ':path': '/Index/GetCategory',
        # 'accept': '*/*',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': m.content_type,
        # 'origin': 'https://msdn.itellyou.cn',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'x-requested-with':'XMLHttpRequest',
        'cookie': 'UM_distinctid175cf967505898-0b05982987527e-75143d4c-13c680-175cf9675066d9; _ga=GA1.2.319749700.1605505546; CNZZDATA1605814=cnzz_eid%3D1910850215-1605505313-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1606097560; _gid=GA1.2.1136103836.1606100781; Hm_lvt_8688ca4bc18cbc647c9c68fdaef6bc24=1605692906,1605753012,1605856840,1606100781; .AspNetCore.Antiforgery.kC_Kc8he0KM=CfDJ8Jw19B-OaM1KveQHPjyyKOMg4zr6PaE4MiX53UQCgjs7sQD--xFt4khM7ij31f6ao9P9lOclj2DbOyfdzXVm6Fuv7l3MVla_6k9YcyFE9_bzMwoWM1_arwOeonh6w_ztsnIfDMb2odn116k1XRy8oOs; _gat=1; Hm_lpvt_8688ca4bc18cbc647c9c68fdaef6bc24=1606102394',
        'x-csrf-token': 'CfDJ8Jw19B-OaM1KveQHPjyyKOOd18a3pjYkGzjpg6yx70hqNG9_vQa70qpa-qQz2D7Eh97RRGkKZgMTkIxKiSSShMstxQsKFw5SS9vir9Rhbqah0HWI45jeBcng-Wa0IPba6xDga6ROzOfyBJAUQ3n7C9E',
        'User-Agent': ua.chrome,
    }
    
    r = requests.post(url='https://msdn.itellyou.cn/Index/GetCategory',data=m  ,headers=my_headers)
    # r.encoding = r.apparent_encoding
    if r.status_code==200:
        return r.text
        list_temp = json.loads(r.text)
        for item in list_temp:
            #将数据保存到数据库
            itellyou_detali(father_key=father_key,key=item['id'],name=item['name']).save()
