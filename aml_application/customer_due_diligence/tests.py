from django.test import TestCase
from .forms import CustomerDueDiligenceForm, CustomerVerificationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from base_app.models import Customer


class CustomerDueDiligenceFormTest(TestCase):

    def test_customer_creation_valid(self):
        form_data = {
            'full_name': 'John Doe',
            'date_of_birth': '1991-01-01',
            'address': '123 Test Street, Auckland',
            'phone': '1234567890',
            'email': 'john@example.com',
            'additional_info': 'Additional information',
        }

        form = CustomerDueDiligenceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_customer_creation_duplicate(self):
        # Create a customer with the same name and date of birth
        Customer.objects.create(
            full_name='John Doe',
            date_of_birth='1991-01-01',
            address='123 Test Street, Auckland',
            phone='1234567890',
            email='john@example.com',
            additional_info='Additional information',
        )

        form_data = {
            'full_name': 'John Doe',
            'date_of_birth': '01-01-1991',
            'address': '123 Test Street, Auckland',
            'phone': '1234567890',
            'email': 'john@example.com',
            'additional_info': 'Additional information',
        }

        form = CustomerDueDiligenceForm(data=form_data)
        self.assertFalse(form.is_valid())


# class CustomerVerificationViewTest(TestCase):
#     def setUp(self):
#         # Create a sample customer
#         self.customer = Customer.objects.create(
#             full_name='John Doe',
#             date_of_birth='1991-01-01',
#         )

#     def test_customer_verification_view(self):
#         # Create a sample uploaded file
#         uploaded_file = SimpleUploadedFile("file.txt", b"file_content")

#         # Create a POST request with form data and file
#         data = {
#             'existing_customer': self.customer.pk,
#             'proof_of_identity': uploaded_file,
#             'proof_of_address': uploaded_file,
#         }

#         response = self.client.post(
#             reverse('verify'), data, follow=True)

#         # Check if the response is successful
#         self.assertEqual(response.status_code, 200)

#         # Check if the customer is verified
#         self.customer.refresh_from_db()
#         self.assertTrue(
#             response.context['existing_customer'].identity_verified)
#         self.assertTrue(response.context['existing_customer'].address_verified)
