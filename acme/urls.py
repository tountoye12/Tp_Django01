"""acme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin

from . import views

handler404 ='acme.views.handler404'
handler404 ='acme.views.handler500'

urlpatterns = [
     url(r'^$', views.home, name='home'),

      url(r'^$', include('account.urls')),

     url(r'^about/', views.about, name='about'),

     url(r'^contact/', views.contact, name='contact'),

     url(r'^blog/', include('blog.urls')),

     url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        #path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
         url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
