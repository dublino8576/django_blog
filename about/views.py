from django.shortcuts import render

from about.models import About

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
    print(f"About object: {about}")
    if about:
        print(f"Title: {about.title}")
        print(f"Content: {about.content}")
        print(f"Updated: {about.updated_on}")
    return render(
        request,
        'about/about.html',
        {'about': about}
    )