from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from course.models import Course
from user_profile.models import Profile

class CourseTestViews(TestCase):
    def setUp(self):
        self.user_staff = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )
        self.group_staff = Group.objects.create(name='staff')
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.user_staff_profile = Profile.objects.create(user=self.user_staff, course=self.course)
        self.user_staff.groups.add(self.group_staff)

    def test_index_view(self):
        self.client.force_login(self.user_staff)
        url = reverse('course:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/index.html')

    def test_delete_view(self):
        self.client.force_login(self.user_staff)
        url = reverse('course:delete', kwargs={'primary_key': self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
    def tearDown(self):
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()