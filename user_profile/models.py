from django.db import models

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

    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=OTHERS)
    student_number = models.CharField(max_length=100, unique=True)
    student_contact_no = models.CharField(max_length=15, unique=True)