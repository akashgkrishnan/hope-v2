from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class management_user(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    user_name = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'