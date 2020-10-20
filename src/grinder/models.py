from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#    "Whether you want to uncover the secrets of the universe, or you want to pursue a career in the 21st century, basic computer programming is an essential skill to learn."
#                                                                           ~Stephen Hawking~

class User (AbstractUser):
    pass
    access_token = models.CharField(blank=True, default= None, max_length = 200, null=True)
    refresh_token = models.CharField(blank=True, default= None, max_length = 200, null=True)
    expires_in = models.IntegerField(blank=True, default= None, null=True)

    def __str__(self):
        return self.username
