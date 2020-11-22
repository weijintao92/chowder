#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Date:2020-10
#Author:wjt
#description: 爬取“我告诉你”网址的数据

from bs4 import BeautifulSoup

from MyApi.myfunction import my_public_method


# from MyApi.models import itellyou
from MyApi.models import itellyou


def itellyou_base():
    """
    获取”我告诉你“基础数据
    """
    r_text = my_public_method.get_url("https://msdn.itellyou.cn/")
    # https://msdn.itellyou.cn/Index/GetCategory
    # AFF8A80F-2DEE-4BBA-80EC-611AC56D3849
    # <h4 class=panel-title><a href=javascript:void(0) data-toggle=collapse data-parent=#accordion
    #                                 data-loadmenu=true data-menuid=AFF8A80F-2DEE-4BBA-80EC-611AC56D3849
    #                                 data-target=#collapse_AFF8A80F-2DEE-4BBA-80EC-611AC56D3849>&#x4F01;&#x4E1A;&#x89E3;&#x51B3;&#x65B9;&#x6848;</a>
    #                         </h4>
    #开始解析数据
    soup = BeautifulSoup(r_text, "html.parser")
    catalogues = soup.find_all(attrs={"data-parent": "#accordion"} )
    list_temp = []
    for item in catalogues:
        my_key = item.get('data-menuid')
        my_name = item.get_text()
        # list_temp.append({"key":my_key,"name":my_name})
        itellyou(key=my_key,name=my_name).save()
    # itellyou.save()



    
        


# if __name__ == '__main__':
#     itellyou_base()