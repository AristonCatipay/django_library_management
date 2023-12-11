from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from thesis.models import Thesis, Author, Author_List
from course.models import Course
from user_profile.models import Profile

class ThesisTestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='firstname test',
            last_name='lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.user_staff = User.objects.create_user(
            first_name='firstname staff',
            last_name='lastname staff',
            username='testuser staff',
            email='emailtest staff',
            password='12345'
        )
        self.group_staff = Group.objects.create(name='staff')
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.user_staff_profile = Profile.objects.create(user=self.user_staff, course=self.course)
        self.user_staff.groups.add(self.group_staff)
        
        self.thesis = Thesis.objects.create(
            title='Thesis title test',
            date_published='2023-3-3',
            course=self.course,
        )

        self.author = Author.objects.create(
            name='Author test',
            first_name='Firstname test',
            last_name='Lastname test',
            course=self.course,
        )
        
        self.author_list = Author_List.objects.create(
            thesis=self.thesis,
            author=self.author,
        )

    def test_index_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/index.html')

    def test_add_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/form.html')

        data = {
            'title': 'This is a thesis title.',
            'date_published': '2012-03-03',
            'course': self.course.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Thesis):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_detail_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:detail', kwargs={'primary_key': self.thesis.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/detail.html')

    def test_edit_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:edit', kwargs={'primary_key' : self.thesis.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/form.html')

        data = {
            'title': 'This is an edited thesis title.',
            'date_published': '2013-03-03', 
            'course': self.course.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Thesis):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)
    
    def test_add_author_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:add_author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/form.html')

        data = {
            'first_name' : 'Add Author Firstname',
            'last_name' : 'Add Author Lastname',
            'course' : self.course.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Author):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_add_author_in_author_list_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('thesis:add_author_in_author_list', kwargs={'primary_key' : self.thesis.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/form.html')

        data = {
            'author' : self.author.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Author in Author List):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)
        
    def tearDown(self):
        # Delete related Thesis instances first
        related_theses = Thesis.objects.filter(course=self.course)
        for thesis in related_theses:
            author_lists = Author_List.objects.filter(thesis=thesis)
            author_lists.delete()
            thesis.delete()

        # Delete Authors associated with the Course
        related_authors = Author.objects.filter(course=self.course)
        related_authors.delete()

        # Then delete remaining related objects
        self.author_list.delete()
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()
        self.user.delete()
