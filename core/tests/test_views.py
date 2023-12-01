from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class CoreViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'core/home.html')

    def test_logout_view(self):
        self.client.force_login(self.user)
        url = reverse('core:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def tearDown(self):
        self.user.delete()