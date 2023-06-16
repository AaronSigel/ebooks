from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

def get_file_upload_path(instance, filename):
    return 'books_files/{author}/{filename}'.format(author=instance.author, filename=filename)

def get_image_upload_path(instance, filename):
    return 'books_images/{author}/{filename}'.format(author=instance.author, filename=filename)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    genres = [('', 'Unspecified'), ('fantasy', 'Fantasy'), ('romance', 'Romance'),
              ('horror', 'Horror'), ('drama', 'Drama'), ('comedy', 'Comedy'), ('sci-fi', 'Sci-Fi'), ('dystopia', 'Dystopia')]
    genre = models.CharField(max_length=100, choices=genres, default='Unspecified')

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    file = models.FileField(upload_to=get_file_upload_path,
                            null=True,
                            blank=True,
                            validators=[FileExtensionValidator(['pdf', 'fb2', 'epub', 'txt'])])

    image = models.ImageField(upload_to=get_image_upload_path)

    def __str__(self):
        return self.title
