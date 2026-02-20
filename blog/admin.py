from django.contrib import admin
from .models import Post, Comment # Import the Post and Comment models from the current app's models.py file to register them with the Django admin site, allowing us to manage posts and comments through the admin interface.
from django_summernote.admin import SummernoteModelAdmin # Import the SummernoteModelAdmin class from django_summernote to use it as a base class for our PostAdmin class, which will allow us to use the Summernote rich text editor for the content field in the Post model when managing posts through the admin interface.

@admin.register(Post) # Register the Post model with the admin site using the PostAdmin class to customize the admin interface for the Post model. (decorator syntax is used here to register the model with the admin site, which is an alternative to using admin.site.register(Post, PostAdmin)), best to use it when you have a custom admin class for the model.
class PostAdmin(SummernoteModelAdmin): #Create a PostAdmin class that inherits from SummernoteModelAdmin to customize the admin interface for the Post model.
    list_display = ('title', 'slug', 'status', 'created_on') # Specify the fields to display in the list view of the admin interface for the Post model.
    search_fields = ['title', 'content'] # Specify the fields to include in the search functionality of the admin interface for the Post model.
    list_filter = ('status', 'created_on',) # Specify the fields to include in the filter sidebar of the admin interface for the Post model.
    prepopulated_fields = {"slug": ("title",)} # Prepopulate the 'slug' field based on the value of the 'title' field in the admin interface.
    summernote_fields = ('content',) # Specify that the 'content' field in the Post model should use the Summernote rich text editor in the admin interface.


# Register your models here.


admin.site.register(Comment) # Register the Comment model with the admin site, which will allow us to manage comments through the Django admin interface.

