from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='author_images', default='default_profile_image.jpg')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='book_images/cover', default='default_book_image.jpg')
    overview_image = models.ImageField(upload_to='book_images/overview', default='default_book_overview_image.jpg')
    table_of_contents_image = models.ImageField(upload_to='book_images/table_of_contents', default='default_book_table_of_contents_image.jpg')
    isbn_number = models.CharField(max_length=255)
    date_published = models.DateField(null=True)
    inventory = models.IntegerField()
    rack_number = models.CharField(max_length=255)
    rack_level_number = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Author_List(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.book.title

