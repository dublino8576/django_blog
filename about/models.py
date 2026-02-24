from django.db import models
from cloudinary.models import CloudinaryField #import the CloudinaryField to use for storing images in the cloud
# Create your models here.

class About(models.Model):

    title = models.CharField(max_length=200) #title of the about page
    content = models.TextField() #content of the about page
    updated_on = models.DateTimeField(auto_now=True) #date and time when the about page was last updated
    profile_image = CloudinaryField('image', default='placeholder') #profile image for the about page, stored in the cloud using Cloudinary
    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"