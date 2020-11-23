from django.conf.urls import url
from MyApi import views

urlpatterns = [
    url(r'^GetVideoUrls/$', views.GetVideoUrls),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    # url(r'', views.GetVideoUrls),
    url(r'^get_itellyou_base/$', views.get_itellyou_base),
    url(r'^reptile_itellyou_base/(?P<pk>[wjt]{3}[A-Za-z0-9]{3})/$', views.reptile_itellyou_base),
]