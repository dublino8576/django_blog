from django.shortcuts import render
from django.views import generic #import the generic view to create a class based view
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) #specifies the queryset to use for this view, in this case it will return all the posts in the database
    template_name = 'post_list.html' #specifies the template to use for this view, if not specified it will look for a template called post_list.html by default