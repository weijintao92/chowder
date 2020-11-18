from django.conf.urls import url
from VideoApi import views

urlpatterns = [
    url(r'^GetVideoUrls/$', views.GetVideoUrls),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]