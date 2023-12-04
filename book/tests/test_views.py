from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from book.models import Book, Author, Author_List
from course.models import Course
from user_profile.models import Profile

class BookTestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.user_staff = User.objects.create_user(
            first_name = 'firstname staff',
            last_name = 'lastname staff',
            username='testuser staff',
            email='emailtest staff',
            password='12345'
        )
        self.group_staff = Group.objects.create(name='staff')
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.user_staff_profile = Profile.objects.create(user=self.user_staff, course=self.course)
        self.user_staff.groups.add(self.group_staff)
        
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

        self.author = Author.objects.create(
            name = 'Author test',
            first_name = 'Firstname test',
            last_name = 'Lastname test',
        )
        
        self.author_list = Author_List.objects.create(
            book = self.book,
            author = self.author,
        )

    def test_index_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('book:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/index.html')

    def test_add_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('book:add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/form.html')

        data = {
            'title': 'This is a book title.',
            'isbn_number': '201922456938',
            'date_published': '2012-03-03', 
            'inventory': 3,
            'rack_number': 3,
            'rack_level_number': 3,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Book):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)
    
    def test_detail_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('book:detail', kwargs={'primary_key' : self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/detail.html')

    def test_edit_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('book:edit', kwargs={'primary_key' : self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/form.html')

        data = {
            'title': 'This is an edited book title.',
            'isbn_number': '2019111111111',
            'date_published': '2013-03-03', 
            'inventory': 4,
            'rack_number': 4,
            'rack_level_number': 4,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Book):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_add_author_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('book:add_author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/form.html')

        data = {
            'name' : 'Add Author Firstname Lastname',
            'first_name' : 'Add Author Firstname',
            'last_name' : 'Add Author Lastname',
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Author):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.author_list.delete()
        related_author_lists = Author_List.objects.filter(book=self.book)
        related_author_lists.delete()
        self.book.delete()
        self.author.delete()
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()
        self.user.delete()
