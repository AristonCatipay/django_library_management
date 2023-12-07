from django.test import TestCase
from django.contrib.auth.models import User
from user_profile.models import Profile
from course.models import Course

class ProfileModelTest(TestCase):
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

    def tearDown(self):
        # Cleanup after each test
        self.profile.delete()
        self.user.delete()
        self.course.delete()

    def test_user_relationship(self):
        expected_user = self.profile.user
        self.assertEqual(expected_user.username, 'testuser')