"""ASB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_default, name='homepage_default'),
    path('home', homepage, name='homepage'),
    path('company', company, name='company'),
    path('expertise', expertise, name='expertise'),
    path('projects', projects, name='projects'),
    path('join', join, name='join'),
    path('media', media, name='media'),
    path('emailsender/', emailsender, name='emailsender'),
    path('expertise_aluminium', expertise_aluminium, name='expertise_aluminium'),
    path('expertise_interior', expertise_interior, name='expertise_aluminium'),
    path('expertise_steel', expertise_steel, name='expertise_aluminium'),
]
