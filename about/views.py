from django.shortcuts import render

from about.models import About
from .forms import CollaborateForm
# Create your views here.
#import messages framework
from django.contrib import messages
def about_me(request):
    '''
    Display the about page.
    
    **Context**
    
    ``about``
        An instance of the :model:`about.About` model.
    
    **Template:**

    :template:`about.html`
    '''

    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST) # Create an instance of the form with POST data
        if collaborate_form.is_valid():
            collaborate_form.save() # Save the form data to the database
            messages.add_message(request, 
            messages.SUCCESS, 'Collaboration request received! I endeavour to respond within 2 working days.') # Add a success message
    about = About.objects.all().order_by('-updated_on').first()
    # Debugging: print to console
    collaborate_form = CollaborateForm()
    return render(
        request,
        'about/about.html',
        {'about': about, "collaborate_form": collaborate_form}, 
    )