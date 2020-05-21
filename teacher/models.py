from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from lead.models import grade_section_master, subject_master

# Create your models here.
class teacher_details(models.Model):
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    emp_code = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField(null = True)
    gender = models.CharField(max_length=2, choices=GENDER)
    adress = models.CharField(max_length=25)
    adress2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25, default='New Delhi')
    pincode = models.CharField(max_length=8)
    user_name = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True)

    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('all-teacher')


class grade_class_teacher(models.Model):
    grade_section = models.OneToOneField(grade_section_master, on_delete=models.DO_NOTHING)
    teacher = models.OneToOneField(teacher_details, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.teacher} class teacher of {self.grade_section}'

    def get_absolute_url(self):
        return reverse('add-class-teacher')

class teacher_subject_grade_section(models.Model):
    teacher = models.ForeignKey(teacher_details, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(subject_master, on_delete=models.DO_NOTHING)
    grade_section = models.ForeignKey(grade_section_master, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.teacher} teaches {self.subject} for {self.grade_section}'


class department(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class department_head(models.Model):
    department = models.OneToOneField(department, on_delete=models.DO_NOTHING)
    department_leader = models.ForeignKey(teacher_details, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.department} {self.department_leader}'


class planners(models.Model):
    IS_APPROVED = (
        ('submit', 'submit'),
        ('approved', 'approved'),
        ('resubmit', 'resubmit')
    )
    title = models.CharField(max_length=40)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(teacher_details, on_delete=models.DO_NOTHING)
    approver = models.ForeignKey(department_head, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=18, choices=IS_APPROVED, default='submit')

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('teacher-home')


