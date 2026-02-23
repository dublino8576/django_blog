from django.shortcuts import render

from about.models import About
from .forms import CollaborateForm
# Create your views here.

def about_me(request):
    '''
    Display the about page.
    
    **Context**
    
    ``about``
        An instance of the :model:`about.About` model.
    
    **Template:**

    :template:`about.html`
    '''

    
    about = About.objects.all().order_by('-updated_on').first()
    # Debugging: print to console
    collaborate_form = CollaborateForm()
    return render(
        request,
        'about/about.html',
        {'about': about, "collaborate_form": collaborate_form}, 
    )