from django.forms import ModelForm
from django import forms
# models
from .models import teacher_details


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
