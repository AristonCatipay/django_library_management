from django.test import SimpleTestCase
from django.urls import reverse, resolve
from suggestion.views import index

class SuggestionTestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('suggestion:index')
        self.assertEquals(resolve(url).func, index)