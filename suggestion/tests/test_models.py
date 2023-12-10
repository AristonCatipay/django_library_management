from django.test import TestCase
from django.contrib.auth.models import User
from suggestion.models import Suggestion

class SuggestionTestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )
        self.suggestion = Suggestion.objects.create(
            book_title = 'Book Title Test',
            comment =  'I love this book title test',
            created_by = self.user,
        )
    def tearDown(self):
        self.suggestion.delete()
        self.user.delete()

    