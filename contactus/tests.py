from django.test import TestCase
from django.urls import reverse
from django.core import mail


class ContactUsTestCase(TestCase):
    def test_contact_us_form_submission(self):
        # Prepare data for the contact us form
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'This is a test message',
        }

        # Send a POST request to the contact us page with the form data
        response = self.client.post(reverse('contact_us'), data=form_data)

        # Check that the response has a successful status code (e.g., 200)
        self.assertEqual(response.status_code, 200)
