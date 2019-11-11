
from django.conf.urls import url

from . import views
app_name = 'blog'

urlpatterns = [
     url(r'^$', views.index, name='index'),

     url(r'^posts/(?P<id>[0-9]+)$', views.show, name='show'),
]
