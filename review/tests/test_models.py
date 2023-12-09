from django.test import TestCase
from django.contrib.auth.models import User
from review.models import Review, Reviewed_Item
from user_profile.models import Profile
from course.models import Course

class ReviewTestModel(TestCase):
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

        self.review = Review.objects.create(
            review = 'This is a test review.',
            user = self.user,
            profile = self.profile,
        )

    def tearDown(self):
        self.review.delete()
        self.profile.delete()
        self.course.delete()
        self.user.delete()

    def test_review_content(self):
        expected_review = f'{self.review.review}'
        self.assertEqual(expected_review, 'This is a test review.')