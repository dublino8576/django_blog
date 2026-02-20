from django.db import models
from django.contrib.auth.models import User # Import the User model from Django's built-in authentication system to establish a relationship between the Post model and the User model, allowing us to associate each post with a specific user (author).

STATUS = (
    (0, "Draft"),
    (1, "Published")
) # Define a tuple called STATUS to represent the possible status values for a post. The first element of each tuple is the actual value that will be stored in the database, and the second element is a human-readable name for that value. In this case, 0 represents "Draft" and 1 represents "Published". This will be used in the status field of the Post model to indicate whether a post is a draft or has been published. tHIS IS A TUPLE OF TUPLES, WHICH IS A COMMON WAY TO DEFINE CHOICES IN DJANGO MODELS. It saves database space and allows for easy retrieval of the human-readable name when displaying the status of a post in templates or the admin interface.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # A CharField to store the title of the post, with a maximum length of 200 characters. The unique=True parameter ensures that no two posts can have the same title.
    slug = models.SlugField(max_length=200, unique=True) # A SlugField to store a URL-friendly version of the title, with a maximum length of 200 characters. The unique=True parameter ensures that no two posts can have the same slug. (slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs. Slug is a short name for article in publishing. It’s a part of URL which identifies a particular page on a website in an easy to read form.)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # A ForeignKey to establish a relationship between the Post model and the User model. The on_delete=models.CASCADE parameter ensures that if a user is deleted, all their associated posts will also be deleted. The related_name='blog_posts' parameter allows us to access a user's posts using user.blog_posts.
    content = models.TextField() # A TextField to store the content of the post, which can be of any length.
    created_on = models.DateTimeField(auto_now_add=True) # A DateTimeField to store the date and time when the post was created. The auto_now_add=True parameter automatically sets the field to the current date and time when the post is created.
    status = models.IntegerField(choices=STATUS, default=0) # An IntegerField to store the status of the post, with choices defined by the STATUS tuple. The default value is set to 0 (Draft).
    excerpt = models.TextField(blank=True) # A TextField to store an optional excerpt of the post, which can be left blank.
    updated_on = models.DateTimeField(auto_now=True) # A DateTimeField to store the date and time when the post was last updated. The auto_now=True parameter automatically updates the field to the current date and time every time the post is saved.
    class Meta:
        ordering = ['-created_on'] # Define the default ordering for the Post model, which will order posts by their created_on date in descending order (newest first).
    def __str__(self):
        return f"The title of this post is {self.title}" # Define the string representation of the Post model to return the title of the post, which will make it easier to identify posts in the admin interface and other contexts where the post is represented as a string.


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # A ForeignKey to establish a relationship between the Comment model and the Post model. The on_delete=models.CASCADE parameter ensures that if a post is deleted, all its associated comments will also be deleted. The related_name='comments' parameter allows us to access a post's comments using post.comments.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter') # A ForeignKey to establish a relationship between the Comment model and the User model. The on_delete=models.CASCADE parameter ensures that if a user is deleted, all their associated comments will also be deleted. The related_name='commenter' parameter allows us to access a user's comments using user.commenter.
    body = models.TextField() # A TextField to store the content of the comment, which can be of any length.
    approved = models.BooleanField(default=False) # A BooleanField to indicate whether the comment has been approved or not. The default value is set to False, meaning that comments will need to be approved before they are displayed.
    created_on = models.DateTimeField(auto_now_add=True) # A DateTimeField to store the date and time when the comment was created. The auto_now_add=True parameter automatically sets the field to the current date and time when the comment is created.
    updated_on = models.DateTimeField(auto_now=True) # A DateTimeField to store the date and time when the comment was last updated. The auto_now=True parameter automatically updates the field to the current date and time every time the comment is saved.

    class Meta:
        ordering = ['created_on'] # Define the default ordering for the Comment model, which will order comments by their created_on date in ascending order (oldest first).
    def __str__(self):
        return f"Comment {self.post.title} by {self.author.username}" # Define the string representation of the Comment model to return a string that includes the title of the post the comment is associated with and the username of the author of the comment, which will make it easier to identify comments in the admin interface and other contexts where the comment is represented as a string.   