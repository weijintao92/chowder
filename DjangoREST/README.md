# DjangoREST

```
# 创建虚拟环境
python3 -m venv ~/.virtualenvs/djangodev
#进入虚拟环境
source ~/.virtualenvs/djangodev/bin/activate
#退出虚拟环境
deactivate

# 最好先更新一下pip至最新版本
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade pip

# 安装
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uvloop
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Django==3.1.3
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygments # 用于代码高亮
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uvicorn
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  uvicorn gunicorn
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple httptools
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple fake_useragent
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests_toolbelt
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple coreapi


# 验证django
import django
print(django.get_version())

# 创建模型
python manage.py startapp MyApi

python manage.py makemigrations MyApi  # 让 Django 知道我们在我们的模型有一些变更

python manage.py migrate  # 创建表结构

rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations MyApi
python manage.py migrate

# 创建一个项目
django-admin.py startproject djsite

# windows 平台
django-admin startproject movieAnalysis

# 启动服务
python manage.py runserver 0:801

# windows 平台
python manage.py runserver 192.168.25.198:8000

# 框架自动创建数据库结构
python manage.py migrate

# 创建管理员用户
python manage.py createsuperuser

# 创建应用
python manage.py startapp Vue #爬虫
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

#查看开放了哪些端口
netstat -lnpt 

# 结束进程
kill -9

uvicorn DjangoREST.asgi:application --reload --port 5000

```
# nginx
```
nginx -s reload # 重新载入配置文件
nginx -s reopen # 重启 Nginx
nginx -s stop # 停止 Nginx
netstat -lnpt #查看开放了哪些端口
```

# 安装sqlite3
```
wget https://www.sqlite.org/2019/sqlite-autoconf-3270200.tar.gz
tar -zxvf sqlite-autoconf-3270200.tar.gz

tar -zxvf sqlite-autoconf-3330000.tar.gz
cd sqlite-autoconf-3270200
cd sqlite-autoconf-3330000
./configure
make && make install
mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
#添加到~/.bashrc中
export LD_LIBRARY_PATH="/usr/local/lib"
```

- 注意：在安装sqlite时请使用默认目录安装的方式，千万不要指定安装目录。不然python无法找到。
- 参考:https://blog.csdn.net/ginynu/article/details/97172159

- 查看sqlite3版本

```
import sqlite3
sqlite3.sqlite_version
#退出sqlite3
.quit   
```
