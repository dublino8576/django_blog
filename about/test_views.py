#test about views imports

from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200) #confirms that the page is rendered successfully
        self.assertIn(b'About Me', response.content) #confirms that the about me content is included in the page content by checking for the byte string 'About Me' in the response content. This helps ensure that the about page is rendering the correct content and that users will see the expected information when they visit the about page.
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm) #confirms that the collaborate form is included in the context and is an instance of CollaborateForm 
    
    ########################################

    def test_successful_collaborate_form_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)