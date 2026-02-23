from django.db import models

# Create your models here.

class About(models.Model):

    title = models.CharField(max_length=200) #title of the about page
    content = models.TextField() #content of the about page
    updated_on = models.DateTimeField(auto_now=True) #date and time when the about page was last updated

    def __str__(self):
        return self.title