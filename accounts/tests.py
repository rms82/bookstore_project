from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.
class TestSignUp(TestCase):
    username = 'admin1'
    email = 'admin1@gmail.com'

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        Model = get_user_model()
        Model.objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(Model.objects.all().count(), 1)
        self.assertEqual(Model.objects.all()[0].username, self.username)

