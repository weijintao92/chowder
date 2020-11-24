#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Date:2020-10
# Author:wjt
# description: 爬取“我告诉你”网址的数据

from MyApi.models import itellyou, itellyou_detali,itellyou_lang_edition,itellyou_software_message
from MyApi.myfunction import my_public_method
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


def reptile_itellyou_base():
    """
    获取”我告诉你“基础数据
    """
    try:
        r_text = my_public_method.get_url("https://msdn.itellyou.cn/")
        # 开始解析数据
        soup = BeautifulSoup(r_text, "html.parser")
        catalogues = soup.find_all(attrs={"data-parent": "#accordion"})
        itellyou.objects.all().delete()  # 清空所有数据
        for item in catalogues:
            my_key = item.get('data-menuid')
            my_name = item.get_text()
            # list_temp.append({"key":my_key,"name":my_name})
            itellyou(key=my_key, name=my_name).save()
        return True
    except Exception as ex:
        print("itellyou-reptile_itellyou_base"+ex)
        return False


def reptile_itellyou_detail():
    """
    # 向目标网站发起请求，提取详细目录信息

    https://msdn.itellyou.cn/Index/GetCategory
    """
    # 获取数据中的所有基础数据
    obj_itellyoubase = itellyou.objects.all()
    if obj_itellyoubase == "":
        return False
    else:
        for var in obj_itellyoubase:
            # 向目标网站发起POT请求，提取详细目录信息
            list_GetCategory = {'id':var.key}
            r_text = my_public_method.itellyou_post(list_GetCategory,"https://msdn.itellyou.cn/Index/GetCategory")
            
            list_temp = json.loads(r_text)
            for item in list_temp:
                # 将数据保存到数据库
                itellyou_detali(father_key=var.key,
                                key=item['id'], name=item['name']).save()
            print(var.key)
            # 随机暂停1-9秒钟，避免被反爬虫
            time.sleep(random.randint(1,9))     
    return True

def reptile_itellyou_finaldata():
    """ 
    获取我告诉你 最终数据

    获取当前版本，有哪些语言版本
    https://msdn.itellyou.cn/Index/GetLang
    Request Method: POST
    formdata
    id: d15691d5-9208-4a7b-b8f8-b64cf6fb875a


    #根据名称和语言版本获取具体的软件信息
    https://msdn.itellyou.cn/Index/GetList
    Request Method: POST
    formdata
    id: d15691d5-9208-4a7b-b8f8-b64cf6fb875a
    lang: e15db4de-c094-4c50-822a-98ad50daba4f
    filter: true

    """
    # 清空数据
    itellyou_lang_edition.objects.all().delete()
    itellyou_software_message.objects.all().delete()
        # 获取数据中的所有基础数据
    obj_itellyou_detali = itellyou_detali.objects.all()
    if obj_itellyou_detali == "":
        return False
    else:
        for var in obj_itellyou_detali:
            # 向目标网站发起POT请求，提取软件语言版本信息
            list_GetLang_params = {'id':var.key}
            r_lang_text = my_public_method.itellyou_post(list_GetLang_params,"https://msdn.itellyou.cn/Index/GetLang")
            
            list_temp = json.loads(r_lang_text)
            for item in list_temp["result"]:
                # 将数据保存到数据库itellyou_lang_edition
                itellyou_lang_edition(father_key=var.key,
                                key=item['id'], lang=item['lang']).save()
                # 构造请求的参数
                list_software_params = {'id': var.key,'lang':item['id'],'filter': 'true'}
                r_software_text = my_public_method.itellyou_post(list_software_params,"https://msdn.itellyou.cn/Index/GetList")
                list_software_data = json.loads(r_software_text)
                for software_data in list_software_data["result"]:
                    # 保存数据itellyou_software_message
                    itellyou_software_message(father_key=item['id'],key=software_data['id'],name=software_data['name'],edition_date=software_data['post'],download_url=software_data['url']).save()
            print(var.key)
            # 随机暂停1-9秒钟，避免被反爬虫
            time.sleep(random.randint(1,9))     
    return True


# if __name__ == '__main__':
#     post_url()
