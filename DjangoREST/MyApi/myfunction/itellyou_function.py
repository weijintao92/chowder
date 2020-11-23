#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Date:2020-10
#Author:wjt
#description: 爬取“我告诉你”网址的数据

from bs4 import BeautifulSoup

import requests

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

from MyApi.myfunction import my_public_method


from MyApi.models import itellyou


def reptile_itellyou_base():
    """
    获取”我告诉你“基础数据
    """
    try:
        r_text = my_public_method.get_url("https://msdn.itellyou.cn/")
        #开始解析数据
        soup = BeautifulSoup(r_text, "html.parser")
        catalogues = soup.find_all(attrs={"data-parent": "#accordion"} )
        itellyou.objects.all().delete() # 清空所有数据
        for item in catalogues:
            my_key = item.get('data-menuid')
            my_name = item.get_text()
            # list_temp.append({"key":my_key,"name":my_name})
            itellyou(key=my_key,name=my_name).save()
        return True 
    except Exception as ex:
        print("itellyou-reptile_itellyou_base"+ex)
        return False
    

def post_url():
    """
    请求网站公共方法
    """
    
    ua = UserAgent()  # 爬虫请求头伪装
    payload = {'id': 'AFF8A80F-2DEE-4BBA-80EC-611AC56D3849'}
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
        

        # 'User-Agent': ua.chrome,
    }
    
    r = requests.post(url='https://msdn.itellyou.cn/Index/GetCategory',data=m  ,headers=my_headers)
    # r.encoding = r.apparent_encoding
    if r.status_code==200:
        return r.text
        




    
        


# if __name__ == '__main__':
#     post_url()