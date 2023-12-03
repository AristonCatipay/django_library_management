from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from user_profile.models import Profile
from course.models import Course
from book.models import Book
from review.views import add

class ReviewTestUrls(TestCase):
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

        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

    def test_add_url(self):
        self.client.force_login(self.user)
        url = reverse('review:add', kwargs={'book_id': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review/form.html')

        data = {
            'review': 'This is a test review'
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Book Review):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.book.delete()