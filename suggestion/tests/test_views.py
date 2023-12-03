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

    def test_index_views(self):
        self.client.force_login(self.user)
        url = reverse('suggestion:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'suggestion/index.html')

    def test_add_views(self):
        self.client.force_login(self.user)
        url = reverse('suggestion:add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'suggestion/form.html')

        data = {
            'book_title': self.suggestion.book_title,
            'comment': self.suggestion.comment, 
            'created_by': self.suggestion.created_by,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Suggestion):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.suggestion.delete()
        self.user.delete()