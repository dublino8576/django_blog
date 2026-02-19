from . import views #import the views from the current directory (the blog app)
from django.urls import path # import the path function to create urls

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), #create a url for the root url that uses the PostList view and names it 'home'
    ] #as_view() is a method that converts the PostList class into a view that can be used in the url patterns