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


from MyApi.models import itellyou,itellyou_detali


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
    

def reptile_itellyou_detail():
    """
    请求网站公共方法
    """
    list_itellyoubase = itellyou.objects.all()
    if len(list_itellyoubase):
        pass

    for target_list in list_itellyoubase:
        my_public_method.itellyou_post(target_list["key"])
        




    
        


# if __name__ == '__main__':
#     post_url()