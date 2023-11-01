from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Review(models.Model):
    review = models.CharField(max_length=255)

class ReviewedItem(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Type: Books, Thesis
    object_id = models.PositiveIntegerField()
    # ID of that object
    # Assuming every table has a primary key and all primary key are positive.
    content_object = GenericForeignKey()
    # Getting the actual object.
