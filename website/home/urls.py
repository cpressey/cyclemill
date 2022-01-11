from django.urls import include, path

from django.conf.urls import url

from home import views


urlpatterns = [
    url(r'^$', views.home,),
]
