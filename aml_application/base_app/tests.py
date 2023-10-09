from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile


class AuthenticationTests(TestCase):
    def test_registration(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('register'),
            {
                'email': 'test@example.com',
                'password1': 'testpassword',
                'password2': 'testpassword',
                'userType': 'tAcsp',
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_login(self):
        # Create a user
        user = User.objects.create_user(
            username='test@example.com',
            email='test@example.com',
            password='testpassword'
        )

        # Log the user in
        response = self.client.login(
            username='test@example.com',
            password='testpassword'
        )

        # Check if the user is logged in
        self.assertTrue(response)

        # Optionally, you can check if the user is redirected to the expected URL
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
