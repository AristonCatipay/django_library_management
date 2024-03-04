from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from suggestion.views import index, create_suggestion, edit
from suggestion.models import Suggestion

class SuggestionTestUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )
        self.suggestion = Suggestion.objects.create(
            book_title = '',
            comment = '',
            created_by = self.user,
        )

    def test_index_url(self):
        url = reverse('suggestion:index')
        self.assertEquals(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('suggestion:add')
        self.assertEquals(resolve(url).func, create_suggestion)

    def test_edit_url(self):
        url = reverse('suggestion:edit', args=[self.suggestion.pk])
        self.assertEquals(resolve(url).func, edit)

    def tearDown(self):
        self.suggestion.delete()
        self.user.delete()