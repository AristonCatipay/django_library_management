from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user_profile.models import Profile
from course.models import Course

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.course = Course.objects.create(
            name = 'Test Course',
            abbreviation = 'TC',
        )

        self.profile = Profile.objects.create(
            user = self.user,
            image = 'media/default_profile_image.jpg',
            gender = 'O',
            student_number = '2019112233',
            student_contact_no = '09123456789',
            course = self.course,
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('profile:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'user_profile/index.html')

    def test_edit_view(self):
        self.client.force_login(self.user)
        url = reverse('profile:edit')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/edit.html')

        data = {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'username': self.user.username,
            'email': self.user.email,
            'password': self.user.password,
            'gender': self.profile.gender,
            'student_number': self.profile.student_number,
            'student_contact_no': self.profile.student_contact_no,
            'course' : self.profile.course,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Profile edit):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)
    
    def tearDown(self):
        # Cleanup after each test
        self.profile.delete()
        self.user.delete()
        self.course.delete()