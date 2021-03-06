from django.conf.urls import url
from MyApi import reptileViews
from MyApi import getViews

urlpatterns = [
    url(r'^GetVideoUrls/$', getViews.GetVideoUrls),
    url(r'^get_itellyou_base/$', getViews.get_itellyou_base),
    url(r'^get_itellyou_detail/$', getViews.get_itellyou_detail),
    url(r'^get_itellyou_lang_edition/$', getViews.get_itellyou_lang_edition),
    url(r'^get_itellyou_software_message/$', getViews.get_itellyou_software_message),

    url(r'^reptile_itellyou_base/(?P<pk>[wjt]{3}[A-Za-z0-9]{3})/$', reptileViews.reptile_itellyou_base),
    url(r'^reptile_itellyou_detail/(?P<pk>[wjt]{3}[A-Za-z0-9]{3})/$', reptileViews.reptile_itellyou_detail),
    url(r'^reptile_itellyou_finaldata/(?P<pk>[wjt]{3}[A-Za-z0-9]{3})/$', reptileViews.reptile_itellyou_finaldata),
]