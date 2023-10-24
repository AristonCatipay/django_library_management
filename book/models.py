from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='book_images/cover', default='default_book_image.jpg')
    overview_image = models.ImageField(upload_to='book_images/overview', default='default_book_overview_image.jpg')
    table_of_contents_image = models.ImageField(upload_to='book_images/table_of_contents', default='default_book_table_of_contents_image.jpg')
    isbn_number = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_published = models.DateField(null=True)
    inventory = models.IntegerField()
    rack_number = models.CharField(max_length=255)
    rack_level_number = models.CharField(max_length=255)