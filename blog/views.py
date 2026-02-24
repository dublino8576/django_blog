from django.shortcuts import render
from django.views import generic #import the generic view to create a class based view
from .models import Post, Comment #import the Post and Comment models to use in the views
from django.shortcuts import get_object_or_404 #import the get_object_or_404 function to get an object from the database or return a 404 error if it does not exist
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
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

def comment_edit(request, slug, comment_id):
    '''
    Edit an existing comment.
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id) #PK stands for primary key, it is used to get the comment object from the database based on the comment_id passed in the URL
    comment_form = CommentForm(data=request.POST, instance=comment)

    if comment_form.is_valid() and comment.author == request.user:
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.approved = False
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
    else:
        messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
#this view allows users to edit their comments. It checks if the comment form is valid and if the user is the author of the comment before saving the changes. If the comment is successfully updated, a success message is displayed. If there is an error, an error message is displayed. After processing the form, the user is redirected back to the post detail page.
#CHECKING IF AUTHOR OF COMMENT IS SAME AS USER MAKING REQUEST TO EDIT COMMENT BECAUSE WE ONLY WANT THE AUTHOR OF THE COMMENT TO BE ABLE TO EDIT IT. IF THE USER IS NOT THE AUTHOR, THEY WILL NOT BE ABLE TO EDIT THE COMMENT AND AN ERROR MESSAGE WILL BE DISPLAYED. (SECURITY MEASURE TO PREVENT USERS FROM EDITING OTHER USERS' COMMENTS)


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
#DELETE_VIEW: This view allows users to delete their comments. It checks if the user making the request is the author of the comment before allowing the deletion. If the user is the author, the comment is deleted and a success message is displayed. If the user is not the author, an error message is displayed. After processing the deletion, the user is redirected back to the post detail page. This ensures that only the author of a comment can delete it, providing a layer of security and preventing unauthorized deletions.