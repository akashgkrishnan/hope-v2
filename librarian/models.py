from django.db import models
from student.models import student_details
from django.utils import timezone

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
    

class books_out(models.Model):
    book = models.ForeignKey(book_inventory, on_delete= models.CASCADE)
    student = models.ForeignKey(student_details, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=timezone.now)
    returned_date = models.DateTimeField(blank=True)
    is_returned = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.student} has been assigned {self.book}'
    

    
    


