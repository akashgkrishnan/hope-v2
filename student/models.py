from django.db import models
from django.contrib.auth.models import User
from lead.models import grade_section_master, bus_master
from teacher.models import grade_class_teacher

# Create your models here.
class student_details(models.Model):  # for storing student info
    STATUS_TYPES = (
        ('S', 'STUDYING'),
        ('PO', 'PASSED OUT'),
        ('D', 'DISMISSED'),
        ('AD', 'ADMISSION DONE'),
        ('LS', 'LEAVE SCHOOL')
    )
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    first_name = models.CharField(max_length=20,)
    last_name = models.CharField(max_length=20)
    admission_number = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=3, choices=STATUS_TYPES, default='S')
    gender = models.CharField(max_length=2, choices=GENDER)
    fathers_name = models.CharField(max_length=40)
    mothers_name = models.CharField(max_length=40)
    dob = models.DateField(verbose_name="DOB")
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    grade_section = models.ForeignKey(grade_section_master, on_delete=models.DO_NOTHING)
    user_name = models.ForeignKey(User, on_delete = models.DO_NOTHING)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class student_address(models.Model):
    student = models.ForeignKey(student_details, on_delete=models.DO_NOTHING)
    adress = models.CharField(max_length=25)
    adress2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25, default='New Delhi')
    pincode = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.student} address'


class student_bus_info(models.Model):
    student = models.OneToOneField(student_details, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_master,on_delete= models.DO_NOTHING)
    start_point = models.CharField(max_length = 20)
    end_point = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.student} takes {self.bus}'


class student_attendance(models.Model):
    ATTENDANCE_TYPE = (
        ('PRESENT', 'PRESENT'),
        ('ABSENT', 'ABSENT'),
        ('APPLIED LEAVE','APPLIED LEAVE'),
        ('HOLIDAY', 'HOLIDAY'),
        ('OTHER', 'OTHER')
    )
    student = models.ForeignKey(student_details, on_delete=models.DO_NOTHING)
    attended = models.CharField(max_length=16, choices=ATTENDANCE_TYPE, default='PRESENT')
    date = models.DateField()



class attendance_history(models.Model):
    attendance_of = models.ForeignKey(grade_class_teacher, on_delete= models.DO_NOTHING)
    attended_on = models.DateField()

    def __str__(self):
        return f'attendance of {self.attendance_of.grade_section} has been marked for the day of {self.attended_on}'