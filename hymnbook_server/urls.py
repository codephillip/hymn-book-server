from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/hymns$', views.hymns_route, name='hymns_route'),
    url(r'^api/v1/categorys$', views.categorys_route, name='categorys_route')
]
