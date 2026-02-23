from . import views #import the views from the current directory (the blog app)
from django.urls import path # import the path function to create urls
from django.contrib import admin

urlpatterns = [
    path('', views.about_me, name='about'), #create a url for the root url that uses the about view and names it 'about'
    ] 