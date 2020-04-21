from django.forms import ModelForm
from django import forms
from .models import lead_user, bus_master, event


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