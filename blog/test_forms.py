from django.test import TestCase
from .forms import CommentForm
# Create your tests here.
# Run python manage.py test: It runs all the tests in the project and provides feedback on whether they passed or failed. This is essential for ensuring that your code is working as expected and helps catch any bugs or issues early in the development process. By running tests regularly, you can maintain the quality and reliability of your application as you make changes and add new features.

class TestCommentForm(TestCase):
    #REMEMBER: class methods must start with 'test' to be recognized as test cases by the testing framework. This is a convention that allows the testing framework to automatically discover and run the tests when you execute the test command. By following this naming convention, you ensure that your test methods are executed and that you receive feedback on their success or failure when running your tests.
    def test_form_is_valid(self):
        comment_form = CommentForm({
            'body': 'This is a great post'
        })
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid') # Test that the form is valid when a body is provided and assert that the form's is_valid() method returns True. If the form is not valid, the test will fail and the message 'Form is not valid' will be displayed to indicate the reason for the failure. This helps ensure that the form validation logic is working correctly and that the form can be successfully submitted when valid data is provided.
    
    def test_form_is_invalid(self):
        comment_form = CommentForm({
            'body': ''
        })
        self.assertFalse(comment_form.is_valid(), msg='Form is valid') # Test that the form is invalid when the body is empty and assert that the form's is_valid() method returns False. If the form is valid, the test will fail and the message 'Form is valid' will be displayed to indicate the reason for the failure. This helps ensure that the form validation logic is working correctly and that the form cannot be submitted when required data is missing or invalid.