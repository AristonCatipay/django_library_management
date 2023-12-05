from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from thesis.models import Thesis, Author, Author_List
from course.models import Course
from user_profile.models import Profile

class ThesisTestViews(TestCase):
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
        
        self.thesis = Thesis.objects.create(
            title = 'Thesis title test',
            date_published = '2023-3-3',
            course = self.course,
        )

        self.author = Author.objects.create(
            name = 'Author test',
            first_name = 'Firstname test',
            last_name = 'Lastname test',
            course = self.course,
        )
        
        self.author_list = Author_List.objects.create(
            thesis = self.thesis,
            author = self.author,
        )

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

