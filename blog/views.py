from django.shortcuts import render
from django.views import generic #import the generic view to create a class based view
from .models import Post, Comment #import the Post and Comment models to use in the views
from django.shortcuts import get_object_or_404 #import the get_object_or_404 function to get an object from the database or return a 404 error if it does not exist
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) #specifies the queryset to use for this view, in this case it will return all the posts in the database
    template_name = 'blog/index.html' #specifies the template to use for this view, if not specified it will look for a template called post_list.html by default
    paginate_by = 6 #specifies the number of posts to display per page, in this case it will display 6 posts per page

def post_detail(request, slug):
    '''
    Display an individual :model:`blog.Post` based on the slug passed in the URL.
    
    **Context**
    
    ``post``
        An instance of the :model:`blog.Post` model.
    
    **Template:**

    :template:`blog/post_detail.html`
    '''
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on") #get all the comments for the post and order them by the date they were created
    comment_count = post.comments.filter(approved=True).count()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_count': comment_count})