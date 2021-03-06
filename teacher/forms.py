from django.forms import ModelForm
from django import forms
# models
from .models import teacher_details, department_head, department, grade_class_teacher, teacher_subject_grade_section


class DateInput(forms.DateInput):
    input_type = 'date'



class TeacherForm(ModelForm):
    class Meta:
        model = teacher_details
        fields = [
            'first_name',
            'last_name',
            'emp_code',
            'mobile',
            'email',
            'date_of_joining',
            'gender',
            'adress',
            'adress2',
            'city',
            'state',
            'pincode']

        widgets = {
            'date_of_joining': DateInput()
        }


class departmentForm(ModelForm):
    class Meta:
        model = department
        fields = '__all__'

class departmentHeadForm(ModelForm):
    class Meta:
        model = department_head
        fields = ['department_leader']


class gradeClassTeacherForm(ModelForm):
    class Meta:
        model = grade_class_teacher
        fields = '__all__'
        

class subjectTeachersForm(ModelForm):
    class Meta:
        model = teacher_subject_grade_section
        fields = '__all__'