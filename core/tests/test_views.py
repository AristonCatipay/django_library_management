# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User

# class CoreViewTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')

#     def test_home_view(self):
#         url = reverse('core:home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response ,'core/home.html')

#     def test_index_view(self):
#         self.client.force_login(self.user)
#         url = reverse('core:index')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response ,'core/index.html')

#     def test_signin_view(self):
#         url = reverse('core:signin')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response ,'core/signin.html')

#         data = {
#             'username': self.user.username,
#             'password': self.user.password,
#         }

#         response = self.client.post(url, data)
#         print("\nTest Data Used (Sign in):", data, "\n")

#         if response.context:
#             # Retrieve form instance to access errors
#             form = response.context['form']
#             if form.errors:
#                 print(form.errors)

#         self.assertEqual(response.status_code, 302)

#     def test_signup_view(self):
#         url = reverse('core:signup')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response ,'core/signup.html')

#         data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'username': 'john.doe',
#             'email': 'john.doe@gmail.com',
#             'password': '12345',
#             'confirm_password': '12345',
#         }

#         response = self.client.post(url, data)
#         print("\nTest Data Used (Sign up):", data, "\n")

#         if response.context:
#             # Retrieve form instance to access errors
#             form = response.context['form']
#             if form.errors:
#                 print(form.errors)

#         self.assertEqual(response.status_code, 302)

#     def test_signout_view(self):
#         self.client.force_login(self.user)
#         url = reverse('core:signout')
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 302)
#         self.assertNotIn('_auth_user_id', self.client.session)
    
#     def tearDown(self):
#         self.user.delete()