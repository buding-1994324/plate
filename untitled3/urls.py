"""untitled3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]
# from django.contrib import admin
# from django.conf.urls import include,url
# from focus import urls as focus_urls
# from focus import views

# urlpatterns = [
# #     # url(r'^$','cms.views.home',name='home'),
# #     url(r'^focus/',include(focus_urls)),
# #     url(r'^$',views.index,name='index'),
# #     url(r'^admin/',include(admin.site.urls))
# # ]

from django.conf.urls import include, url
from django.contrib import admin
from focus import urls as focus_urls
from focus import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^focus/', include(focus_urls)),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]