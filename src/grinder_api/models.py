from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
models.AutoField(primary_key=True)

# Create your models here.
class grinderuser(User):
        spid = models.CharField(max_length = 300, default=None, blank=True, null=True)
        def __str__(self):
            return self.username
pass



class Track(models.Model):
        id = models.AutoField(primary_key=True)#Django gives each model this field by default
        spid = models.CharField(max_length = 300,default=None, blank=True, null=True)
        name = models.CharField(max_length = 300)
        duration_ms = models.IntegerField()
        href = models.CharField(max_length = 300)
        owner = models.ForeignKey(grinderuser, on_delete=models.CASCADE, editable=False, default=None, blank=True, null=True)
        stream_source = models.CharField(max_length = 1000, help_text = "Copy and paste the URL link to the song")

        def __str__(self):
            return self.name
