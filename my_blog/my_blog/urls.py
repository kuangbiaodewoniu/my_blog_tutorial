"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from article import views
from article.views import RSSFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/', views.home, name='home'),
    path('detail/', views.detail),
    path('test/', views.test),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    path('archives/', views.archives),
    path('about_me/', views.about_me),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed/$', RSSFeed(), name="RSS"),
]
