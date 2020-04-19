from django.db import models

# Create your models here.
class book_inventory(models.Model):
    GENRES = (
        ('ACTION', 'ACTION'),
        ('ROMANCE', 'ROMANCE'),
        ('THRILLER', 'THRILLER'),
        ('SUSPENSE', 'SUSPENSE'),
        ('COMEDY', 'COMEDY'),
        ('ACADMEDIC', 'ACADEMIC'),
        ('GENERAL', 'GENERAL'),
        ('STORYBOOK', 'STORYBOOK')
    )
    book_name = models.CharField(max_length = 40)
    book_author = models.CharField(max_length = 40)
    genre = models.CharField(max_length = 15, choices=GENRES)
    number_of_books = models.PositiveIntegerField()
    book_number = models.CharField(max_length = 15)

    def __str__(self):
        return self.book_name
