from django.contrib import admin
from .models import Post, Comment # Import the Post and Comment models from the current app's models.py file to register them with the Django admin site, allowing us to manage posts and comments through the admin interface.

# Register your models here.

admin.site.register(Post) # Register the Post model with the admin site, which will allow us to create, edit, and delete posts through the Django admin interface.

admin.site.register(Comment) # Register the Comment model with the admin site, which will allow us to manage comments through the Django admin interface.