"""BlogCoders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from blog import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('bloghome', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('addblog', views.addblog, name='addblog'),
    path('editblog/<str:sno>', views.editblog, name='editblog'),
    path('delete_data/<str:sno>', views.delete_data, name='delete_data'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    
]
