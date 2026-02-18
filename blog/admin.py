from django.contrib import admin
from .models import Post # Import the Post model from the current app's models.py file to register it with the Django admin site, allowing us to manage posts through the admin interface.

# Register your models here.
admin.site.register(Post) # Register the Post model with the admin site, which will allow us to create, edit, and delete posts through the Django admin interface.