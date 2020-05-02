from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class bus_master(models.Model): #conductor nd driver info to be done
    STATUS_TYPES = (
        ('A', 'Active'),
        ('X', 'Inactive')
    )
    bus_reg_number = models.CharField(max_length=12)
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default='A')
    owner_mobile = models.CharField(max_length=12)
    owner_name = models.CharField(max_length=12)
    bus_Route_start_to_end = models.CharField(max_length=65)

    def __str__(self):
        return self.bus_Route_start_to_end

    def get_absolute_url(self):
        return reverse('lead-home')

class section_master(models.Model):
    section_name = models.CharField(max_length=1)

    def __str__(self):
        return self.section_name

class grade_master(models.Model):
    grade_name = models.CharField(max_length=4)

    def __str__(self):
        return self.grade_name

class grade_section_master(models.Model):
    grade = models.ForeignKey(grade_master, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(section_master, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.grade} {self.section}"


class lead_user(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    user_name = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class event(models.Model):
    TYPE = (
        ('CBR', 'CELEBRATIONS'),
        ('HOLIDAYS', 'HOLIDAY'),
        ('GOVT', 'GOVT HOLIDAY'),
        ('OTHER', 'OTHER')
    )
    date = models.DateField()
    name_of_holiday = models.CharField(max_length=45)
    event_type = models.CharField(max_length=15, choices=TYPE)


class subject_master(models.Model):
    subject_name = models.CharField(max_length=65)

    def __str__(self):
        return f'{self.subject_name}'

class subject_and_grade(models.Model):
    subject = models.ForeignKey(subject_master, on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(grade_master, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.subject} ({self.grade})'


class subject_grade_section(models.Model):
    subject = models.ForeignKey(subject_master, on_delete=models.DO_NOTHING)
    grade_section = models.ForeignKey(grade_section_master, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.subject} ({self.grade_section})'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'