from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

#import the necessary modules and classes for testing the views in the blog app. This includes the User model for creating test users, the reverse function for generating URLs, the TestCase class for creating test cases, the CommentForm for testing form validation, and the Post model for creating test posts.

class TestBlogViews(TestCase):

    '''Test the views in the blog app, including the post_detail view which displays an individual blog post and allows users to submit comments. The tests will check that the view renders correctly, that the comment form is included in the context, and that the form validation works as expected when submitting comments.

    The setUp method is used to create a test user and a test post that will be used in the tests. The test_render_post_detail_page_with_comment_form method tests that the post_detail view renders correctly and includes the comment form in the context. It checks that the response status code is 200 (indicating a successful response), that the post title and content are included in the response content, and that the comment form is an instance of CommentForm. This helps ensure that the post_detail view is functioning correctly and that users can submit comments on blog posts as intended.'''
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-title'])) #we use reverse to generate a URL for accessing the post_detail view, providing 'blog-title' as an argument. client.get() is then used to make a GET request to that URL, and the response is stored in the response variable for further assertions and checks in the test. This allows us to test the functionality of the post_detail view and ensure that it renders correctly when accessed with a valid slug.
        
        #When we print response.content to the terminal, we see the full HTML that the browser would use to build that page. We can see both the <head> and <body> content are contained within response.content. This enables us to run tests on it to confirm that the page would be rendered as expected, such as. self.assertIn(b"Blog title", response.content) byte is used because the browser renders data in bytes
        self.assertEqual(response.status_code, 200) # confirms that the view responds successfully, a fundamental check for any web page.

        # Check that the post title and content are included in the response content
        self.assertIn(b"Blog title", response.content) # Check that the post title is included in the response content by asserting that the byte string "Blog title" is present in the response content. This helps ensure that the post_detail view is rendering the correct post and that the post's title is being displayed to the user as expected.
        self.assertIn(b"Blog content", response.content) # Check that the post content is included in the response content by asserting that the byte string "Blog content" is present in the response content. This helps ensure that the post_detail view is rendering the correct post and that the post's content is being displayed to the user as expected.
        self.assertIsInstance(
            response.context['comment_form'], CommentForm) # Check that the comment form is included in the context and is an instance of CommentForm by asserting that the comment_form in the response context is an instance of the CommentForm class. This helps ensure that the post_detail view is including the comment form in the context correctly and that users will be able to submit comments on blog posts as intended.
        #When we print RESPONSE.CONTEXT to the terminal, we see the context object that is passed to the template from the relevant view. This includes our own custom context, such as 'comment_count' and 'comment_form', as well as many other context variables automatically created by Django. This also enables us to run tests on response.context to confirm that the correct objects were passed to the template by the view.

#########################################

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        } #simulate login as superuser and create a dictionary called post_data that contains the data for the comment we want to submit, in this case, the body of the comment is set to 'This is a test comment.' This data will be used to simulate a POST request to the post_detail view to test the comment submission functionality.
        response = self.client.post(reverse(
            'post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        ) # Check that the success message is included in the response content by asserting that the byte string 'Comment submitted and awaiting approval' is present in the response content. This helps ensure that when a comment is successfully submitted, the user receives feedback confirming that their comment has been received and is awaiting approval, which enhances the user experience and provides clarity on the status of their comment submission.

