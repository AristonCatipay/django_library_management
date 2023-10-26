from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    book_title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
