from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', include('home.urls')),
]
