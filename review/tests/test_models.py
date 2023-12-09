from django.test import TestCase
from django.contrib.auth.models import User
from review.models import Review, Reviewed_Item
from user_profile.models import Profile
from course.models import Course
from book.models import Book

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

    def test_review_and_user_relationship(self):
        user = self.review.user
        self.assertEqual(user.username, 'testuser')

    def test_review_and_profile_relationship(self):
        profile = self.review.profile
        self.assertEqual(profile.student_number, '2019112233')


class ReviewItemTestModel(TestCase):
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

        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

        self.review_item = Reviewed_Item.objects.create(
            review = self.review,
            book = self.book
        )

    def tearDown(self):
        self.review_item.delete()
        self.book.delete()
        self.review.delete()
        self.profile.delete()
        self.course.delete()
        self.user.delete()