from django.forms import ModelForm
from django import forms
from django.views.generic.dates import DateMixin
from .models import lead_user, bus_master, event, subject_grade_section, todos
from student.models import (student_details,
                            student_address,
                            student_bus_info)

from teacher.models import grade_class_teacher

class DateInput(forms.DateInput, DateMixin):
    input_type = 'date'
    allow_future = False


class leadForm(ModelForm):
    class Meta:
        model = lead_user
        fields = ['first_name', 'last_name', 'mobile', 'email']


class busForm(ModelForm):
    class Meta:
        model = bus_master
        fields = [
            'bus_reg_number',
            'owner_mobile',
            'owner_name',
            'bus_Route_start_to_end'
        ]


class createEventForm(ModelForm):
    class Meta:
        model = event
        fields = ['date', 'name_of_holiday', 'event_type']
        widgets = {
            'date': DateInput()
        }


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


class subjectSectionForm(ModelForm):
    class Meta:
        model = subject_grade_section
        fields = ['grade_section']

class todoForm(ModelForm):
    class Meta:
        model = todos
        fields = ['task_name']