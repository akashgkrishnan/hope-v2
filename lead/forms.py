from django.forms import ModelForm
from django import forms
from .models import lead_user, bus_master, event
from student.models import (student_details,
                            student_address,
                            student_bus_info)


class DateInput(forms.DateInput):
    input_type = 'date'


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
        fields = '__all__'
        widgets = {
            'dob': DateInput()
        }

class studentAddressForm(ModelForm):
    class Meta:
        model = student_address
        fields = '__all__'

class studentBusForm(ModelForm):
    class Meta:
        model = student_bus_info
        fields = '__all__'