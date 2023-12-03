from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from suggestion.models import Suggestion

class SuggestionTestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )
        self.suggestion = Suggestion.objects.create(
            book_title = 'This is a book title',
            comment = 'This is a comment.',
            created_by = self.user,
        )

    def tearDown(self):
        self.suggestion.delete()
        self.user.delete()