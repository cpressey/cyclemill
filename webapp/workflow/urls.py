from django.conf.urls import url

from workflow import views


urlpatterns = [
    url(r'^$', views.home,),
    url(r'^launch/$', views.launch,),
]
