from django.conf.urls import url
from MyApi import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API文档')

urlpatterns = [
    url(r'^GetVideoUrls/$', views.GetVideoUrls),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    # url(r'', views.GetVideoUrls),
    url(r'itellyou_base', views.reptile_itellyou_base),
    url(r'^reptile_itellyou_base/(?P<pk>[0-9]+)/$', views.reptile_itellyou_base),
]