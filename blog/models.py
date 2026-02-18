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
    created_on = models.DateField(auto_now_add=True) # A DateField to store the date when the post was created. The auto_now_add=True parameter automatically sets the field to the current date when the post is created.
    status = models.IntegerField(choices=STATUS, default=0) # An IntegerField to store the status of the post, with choices defined by the STATUS tuple. The default value is set to 0 (Draft).