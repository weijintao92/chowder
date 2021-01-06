from django.conf.urls import url
from Vue import views

urlpatterns = [
    url(r'^get_gitHub_accessToken/$', views.get_gitHub_accessToken),
]