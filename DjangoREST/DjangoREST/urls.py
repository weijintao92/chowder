from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from django.urls import path, include


urlpatterns = [
    url(r'^', include('MyApi.urls')),
    path('docs/', include_docs_urls(title='我的测试平台接口文档')), 
    path('', include_docs_urls(title='我的测试平台接口文档')), 
    url(r'^admin/', admin.site.urls),
]
