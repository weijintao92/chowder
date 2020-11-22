#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Date:2020-10
#Author:wjt
#description: 根据百度关键字'vip解析'，爬取视频接口

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

def get_video_api():
    """
    目标网站：http://www.876543.net/
    爬取目标网站使用的视频解析接口，随后输出json格式至文件video_result.txt
    """
    #目标网站
    list_target_site = ['http://www.876543.net/',
                        'http://peng3.com/vip/',
                        'http://www.588230.com/v/',
                        'http://tool.liumingye.cn/video/',
                        'http://www.xyjun.com/vip/',
                        'http://www.meiriyixue.cn/jx/'
                        ]
    #结果
    list_api_urls =[]
    #开始工作
    for site_item in list_target_site:
        #目标1 http://www.876543.net/
        r_text = get_url(site_item)
        #开始解析数据
        soup = BeautifulSoup(r_text, "html.parser")
        list_results = soup.find_all('option')
        for item in list_results:     
            value = item.get('value')
            if value == '1':
                print(333333333333)
            if value not in list_api_urls:
                list_api_urls.append(value)
        print('目标：'+site_item+'抓取结束！')
    
    #输出
    with open('video_result.txt', "w") as fs:
        fs.write(json.dumps(list_api_urls))
        fs.close()

    print('抓取结束！')

def check_video_api():
    """
    判断视频接口是否可用
    """

    with open('video_result.txt', "r") as fs:
        os_url = fs.read()
        fs.close()
    list_urls = json.loads(os_url)
    list_ok = []
    for item in list_urls:
        url_temp = check_api(item)
        if url_temp == None:
            continue
        if url_temp not in list_ok:
            list_ok.append(url_temp)
        
    with open('video_result33.txt', "w") as fs:
        fs.write(json.dumps(list_ok))
        fs.close()
    print('检查结束！')
    

def check_api(my_url):

    try:
        ua = UserAgent()  # 爬虫请求头伪装
        # 定制请求头
        my_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=168C7F2BA03828C13272D6BE432D667A; PSTM=1603554287; BAIDUID=168C7F2BA03828C1B773A6F551E13C63:FG=1; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=1447_32844_31660_32723_32230_7516_7605_32115_31708_26350; BD_UPN=12314753; H_PS_645EC=1e7a9EZYBbpG7jVqrrlfiTQfF0KcYUoJLc3nd9Fa7goUgyqHuxQAB358Afc; BA_HECTOR=al85al842ga18008ua1fp8iug0k; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': ua.chrome,
        }
        r = requests.get(url=my_url,  headers=my_headers,timeout=1,  verify=False)
        if r.status_code == 200:
            return r.url
    except Exception:
        print(my_url)

def html_top():
    """
    html头部
    """
    html_top =  """  
        <!doctype html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="renderer" content="webkit">
            <meta name="force-rendering" content="webkit">
            <meta name="applicable-device" content="pc,mobile">
            <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="Keywords" content="格调解析,vip视频解析,vip解析,VIP部落,全民解析,爱奇艺vip解析,优酷vip解析,腾讯VIP解析">
            <meta name="Description" content="格调vip解析析旨在为网友提供免费的vip视频解析服务，让大家不花钱就能观看各大视频网站的收费视频。目前支持腾讯vip解析,爱奇艺vip解析,芒果会员解析,搜狐vip解析,pptv会员解析,优酷vip解析等">
            <title>格调解析-vip视频在线解析</title>
            <link rel="canonical" href="http://www.gd97.xyz/">
            <link rel="shortcut icon" href="favicon.ico" type="image/vnd.microsoft.icon">
            <link rel="icon" href="favicon.ico" type="image/vnd.microsoft.icon"> 
            <base target="_blank">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

            <!-- <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"> -->
            </script>
        </head>
        <style>
            html,
            body {
                width: 100%;
                height: 100%;
            }
        </style>



        <body>
            <!-- {% load static %} -->
            <!-- <img src="{% static "qaqa/ss.jpg" %}" alt="My image"> -->
            <div class="container" style="height: 100%;width: 100%;">
                <div class="row" style="display: flex;justify-content: center;height: 20%;background-color: aqua;">
                    <h1>格调vip解析</h1>
                    <h4>免责声明：本站所有视频资源均来自网络。服务器仅展示第三方网站接口页面，并不存储任何视频资源。因此经由本站搜索所产生
                        的任何结果皆不代表本站立场，本站不对其真实合法性以及版权负责，亦不承担任何法律责任。</h4>
                </div>
                <div class="row" style="margin-top: 2px;">
                    
                    
                        <div class="input-group mb-3"  >
                            <select id="play_api"  >
     """
    return html_top

def html_bottom():
    """
    底部
    """
    html_bottom = """  
    
            </select>
                            <input type="text" id="url"  style=" border-width: 3px; "  autofocus="autofocus" class="form-control" placeholder="电脑使用Ctrl+V粘贴网址-手机直接长按粘贴网址" aria-label="Text input with dropdown button">
                            
                        </div>
                        <div style="display:flex;justify-content: center;align-items: center;width: 100%; margin-top:-14px;" >
                            <button id="play_begin" type="button"   class="btn btn-primary">Go-开始解析</button>
                            <button id="play_full" type="button" style="margin-left: 10px;"  class="btn btn-primary">Go-全屏解析</button>
                        
                            
                        </div>
                        
                </div>
                <div class="row" style="height: 60%;margin-top: 2px;border: 1px solid black;background-image: url(https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=38991626,1512155436&fm=26&gp=0.jpg);">
                    
                    <iframe id="google_esf" name=" google_esf"  src="http://jqaaa.com/jx.php?url=" marginheight="0" marginwidth="0" frameborder="0" width="100%"height="100%" scrolling="no" allowfullscreen="true" allowtransparency="true" ></iframe>
                </div>  
                <div class="row" style="height: 10%;background-color: crimson;">
                    <h4>仅供学习和交流使用！如有侵权请邮件1109765190@qq.com<br>请勿相信视频中的广告及其他信息！</h4>
                    
                </div>
            </div>


            
        <!-- 按钮触发模态框 -->

        <!-- 模态框（Modal） -->
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header" style="display: flex;justify-content: center;">
                        <!-- <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button> -->
                        <h4 class="modal-title" id="myModalLabel">提示</h4>
                    </div>
                    <div class="modal-body"><div class="alert alert-danger">请输入您需要解析的地址！</div></div>
                    <div class="modal-footer">
                        <!-- <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button> -->
                        <button type="button" id="my_close" class="btn btn-primary" style="width: 100%;" data-dismiss="modal">关闭</button>
                    </div>
                </div><!-- /.modal-content -->
            </div><!-- /.modal -->
        </div>
            
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        </body>
        <script type="text/javascript">
            $(document).ready(function () {
                $("#play_begin").click(function () {
                    var url = $("#url").val()
                    if (url=='') {                	
                        $('#myModal').modal('show')
                        
                        return
                    }
                    var play_api = $("#play_api").val()
                    var analysis_url = play_api+url
                    // console.log(analysis_url)
                    $("#google_esf").attr("src", analysis_url)
                });
                $("#play_full").click(function () {
                    var url = $("#url").val()
                    if (url=='') {
                            
                        $('#myModal').modal('show')
                        return
                    }
                    var play_api = $("#play_api").val()
                    var analysis_url = play_api+url
                    window.open(analysis_url);  
                    
                });

                $("#my_close").click(function () {
                    $("#url").focus()
                });
                
            });

        </script>

        </html>






    """
    return html_bottom

def create_html():
    """
    生成电影解析html
    """
    with open('video_result33.txt', "r") as fs:
        os_url = fs.read()
        fs.close()

    list_urls = json.loads(os_url)
    string_itme = ""
    num = 0
    while num< len(list_urls):
        if num==0:
            string_itme += """  <option value=" """ +list_urls[num]+ """" selected="selected">解析线路"""+str(num+1)+"""</option> \n"""
        else:
            string_itme += """  <option value=" """ +list_urls[num]+ """" >解析线路"""+str(num+1)+"""</option> \n"""
        num+=1
        
    with open('gd97/templates/gd97/index.html', "w",encoding="utf-8") as fs:
        fs.write(html_top()+string_itme+html_bottom())
        fs.close()

def get_url_list():
    """
    获取最终的url集合
    """
    with open('./MyApi/myfunction/video_result33.txt', "r") as fs:
        os_url = fs.read()
        fs.close()

    return json.loads(os_url)
# if __name__ == '__main__':
#     # get_video_api()
#     # check_video_api()
#     create_html()


            