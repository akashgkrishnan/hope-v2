from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class role_details(models.Model):
    role_name = models.CharField(max_length=10)

    def __str__(self):
        return self.role_name


class user_role_map(models.Model):
    stamp_user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(role_details, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.stamp_user} as {self.role}"

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'