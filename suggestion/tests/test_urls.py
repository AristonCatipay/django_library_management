from django.test import SimpleTestCase
from django.urls import reverse, resolve
from suggestion.views import index, add

class SuggestionTestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('suggestion:index')
        self.assertEquals(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('suggestion:add')
        self.assertEquals(resolve(url).func, add)