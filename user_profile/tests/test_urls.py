from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_profile.views import index, edit, change_password

class ProfileUrlTestCase(SimpleTestCase):
    def test_index_url(self):
        url = reverse('profile:index')
        self.assertEquals(resolve(url).func, index)

    def test_edit_url(self):
        url = reverse('profile:edit')
        self.assertEquals(resolve(url).func, edit)
        
    