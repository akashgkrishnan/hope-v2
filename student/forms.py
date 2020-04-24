from django.forms import ModelForm
from django import forms
from student.models import (student_details,
                            student_address,
                            student_bus_info)



class DateInput(forms.DateInput):
    input_type = 'date'


class studentForm(ModelForm):
    class Meta:
        model = student_details
        fields = [
            'first_name',
            'last_name',
            'admission_number',
            'gender',
            'fathers_name',
            'mothers_name',
            'dob',
            'mobile',
            'email',
            'grade_section'
        ]
        widgets = {
            'dob': DateInput()
        }


class studentAddressForm(ModelForm):
    class Meta:
        model = student_address
        fields = [
            'adress',
            'adress2',
            'city',
            'state',
            'pincode'
        ]


class studentBusForm(ModelForm):
    class Meta:
        model = student_bus_info
        fields = [
            'bus',
            'start_point',
            'end_point'
        ]