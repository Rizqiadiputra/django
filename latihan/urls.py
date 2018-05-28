"""latihan URL Configuration

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
from django.urls import path
from django.conf.urls import url
# from post import views as post_view
from post.views import (post_home,post_create,post_detail,post_update,post_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_home),
    path('post/create/', post_create),
    url(r'(?P<id>\d+)/$', post_detail, name="detail"),
    # url(r'^post/detail/(?P<id>\d+)/$', post_detail),
    path('post/update/', post_update),
    path('post/delete/', post_delete),    
    
]
