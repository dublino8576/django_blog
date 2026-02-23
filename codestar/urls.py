"""
URL configuration for codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include #import the include function to include urls from the blog app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), #tells django to look in the allauth app for any urls that start with 'accounts/'
    path('summernote/', include('django_summernote.urls')), #tells django to look in the django_summernote app for any urls that start with 'summernote/'
    path('about/', include('about.urls'), name='about-urls'), #tells django to look in the about app for any urls that start with 'about/'
    path('', include('blog.urls'), name='blog-urls'), 
    #tells django to look in the blog app for any urls that start with '',(the root url)
    ]
