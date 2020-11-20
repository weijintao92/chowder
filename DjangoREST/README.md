# DjangoREST
```
# 创建虚拟环境
python3 -m venv ~/.virtualenvs/djangodev
source ~/.virtualenvs/djangodev/bin/activate
deactivate #退出虚拟环境

python -m pip install Django 安装django
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uvloop
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Django==3.1.3
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygments # 用于代码高亮
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uvicorn

#验证django
import django
print(django.get_version())

#创建一个项目
django-admin.py startproject djsite

#windows 平台
django-admin startproject movieAnalysis

#启动服务
python manage.py runserver 0:801


# windows 平台
python manage.py runserver 192.168.25.198:8000

# 框架自动创建数据库结构
python manage.py migrate

#创建管理员用户
python manage.py createsuperuser

#创建应用
python manage.py startapp video #爬虫
python manage.py startapp admm #控制台
python manage.py startapp gd97 #视频解析

```

# Uvicorn 
- Uvicorn is an ASGI server based on uvloop and httptools, with an emphasis on speed.
- https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/uvicorn/
- https://docs.gunicorn.org/en/stable/install.html
- https://www.uvicorn.org/

```
 python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  uvicorn gunicorn

 gunicorn DjangoREST.asgi:application -k uvicorn.workers.UvicornWorker

```


# nginx
```
nginx -s reload # 重新载入配置文件
nginx -s reopen # 重启 Nginx
nginx -s stop # 停止 Nginx

```