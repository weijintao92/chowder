from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    url(r'^MyApi', include('MyApi.urls')),
    url(r'^Vue', include('Vue.urls')),
    path('', include_docs_urls(title='我的接口')), 
    url(r'^admin/', admin.site.urls),
    url(r'^swagger$',schema_view)
]
