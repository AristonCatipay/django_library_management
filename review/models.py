from django.contrib.auth.models import User
from django.db import models
from book.models import Book
from user_profile.models import Profile

class Review(models.Model):
    review = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Reviewed_Item(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    

