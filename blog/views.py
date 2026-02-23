from django.shortcuts import render
from django.views import generic #import the generic view to create a class based view
from .models import Post, Comment #import the Post and Comment models to use in the views
from django.shortcuts import get_object_or_404 #import the get_object_or_404 function to get an object from the database or return a 404 error if it does not exist
# Create your views here.

from .forms import CommentForm

from django.contrib import messages #import the messages framework to display messages to the user after they submit a comment

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
    ``comments``
        All approved comments for the post.
    ``comment_count``
        Count of approved comments.
    ``comment_form``
        Instance of CommentForm for submitting comments.
    
    **Template:**

    :template:`blog/post_detail.html`
    '''
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("created_on")  # type: ignore
    comment_count = post.comments.filter(approved=True).count()  # type: ignore
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()
    
    return render(
        request, 
        'blog/post_detail.html', 
        {
            'post': post, 
            'comments': comments, 
            'comment_count': comment_count,
            'comment_form': comment_form,
        }
    )