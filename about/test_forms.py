from django.test import TestCase
from .forms import CollaborateForm
# Create your tests here.
#Run python manage.py test about to run tests for the about app only. This allows you to focus on testing the specific functionality of the about app without running tests for the entire project, which can save time and resources during development. By running tests for a specific app, you can quickly identify and address any issues or bugs related to that app's functionality.

#python3 manage.py test about.test_forms. TestCollaborateForm

class TestCollaborateForm(TestCase):
    def test_form_is_valid(self):
        '''
        Test for all fields
        '''
        form = CollaborateForm({
            'name': 'Mixi',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg='Form is not valid') 
        # Test that the form is valid when all required fields are provided and assert that the form's is_valid() method returns True. If the form is not valid, the test will fail and the message 'Form is not valid' will be displayed to indicate the reason for the failure. This helps ensure that the form validation logic is working correctly and that the form can be successfully submitted when valid data is provided.

    def test_form_is_invalid(self):
        '''
        Test for empty fields
        '''
        form = CollaborateForm({
            'name': '',
            'email': '',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg='Form is valid') 
        # Test that the form is invalid when all required fields are empty and assert that the form's is_valid() method returns False. If the form is valid, the test will fail and the message 'Form is valid' will be displayed to indicate the reason for the failure. This helps ensure that the form validation logic is working correctly and that the form cannot be submitted when required data is missing or invalid.

    def test_form_is_invalid_email(self):
        '''
        Test for invalid email field
        '''
        form = CollaborateForm({
            'name': 'Mixi',
            'email': 'invalid-email',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Form is valid') 
        # Test that the form is invalid when the email field contains an invalid email address and assert that the form's is_valid() method returns False. If the form is valid, the test will fail and the message 'Form is valid' will be displayed to indicate the reason for the failure. This helps ensure that the form validation logic is working correctly and that the form cannot be submitted when the email field contains an invalid email address.
    
    def test_message_is_required(self):
        '''
        Test that the message field is required
        '''
        form = CollaborateForm({
            'name': 'Mixi',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg='Form is valid') 