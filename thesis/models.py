from django.db import models
from course.models import Course

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='thesis_author_images', default='default_profile_image.jpg')

    def __str__(self):
        return self.name

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateField(null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class AuthorList(models.Model):
    thesis = models.ForeignKey(Thesis, related_name='thesis_id', on_delete=models.PROTECT)
    author = models.ForeignKey(Author, related_name='author_id', on_delete=models.PROTECT)


    

    