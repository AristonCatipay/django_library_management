from django.db import models
from course.models import Course

from django.contrib.auth import get_user_model


User = get_user_model()
 
class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'O'),
    ]

    image = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=OTHERS)
    student_number = models.CharField(max_length=100, unique=True, null=True)
    student_contact_no = models.CharField(max_length=15, unique=True, null=True)
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='course_id', on_delete=models.CASCADE)
