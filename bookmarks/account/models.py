from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return f'Profil uzytkownika {self.user.username}.'


