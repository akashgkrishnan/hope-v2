from django.forms import ModelForm
from .models import management_user

class managementForm(ModelForm):
    class Meta:
        model = management_user
        fields = ['first_name', 'last_name', 'mobile', 'email']