from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
models.AutoField(primary_key=True)

# Create your models here.
class grinderuser(User):
    def __str__(self):
        return self.username

class Playlist(models.Model):
        collaborative = models.BooleanField()#Django field not required
        description = models.CharField(max_length=5000, help_text="Describe your playlist creatively")
        href = models.CharField(max_length = 300)
        #wowner = models.ForeignKey(grinderuser, on_delete=models.CASCADE, editable=False)
        public = models.BooleanField()
        id = models.AutoField(primary_key=True)#Django gives each model this field by default
        name = models.CharField(max_length = 300, help_text = "Enter a name for your playlist")
        #track = models.ForeginKey(Track, related_name = 'playlist')
        uri = models.CharField(max_length = 300)
        def __str__(self):
            return self.name

class Track(models.Model):
        id = models.AutoField(primary_key=True)#Django gives each model this field by default
        name = models.CharField(max_length = 300)
        duration_ms = models.IntegerField()
        href = models.CharField(max_length = 300)
        #wowner = models.ForeignKey(grinderuser, on_delete=models.CASCADE, editable=False)
        stream_source = models.CharField(max_length = 1000, help_text = "Copy and paste the URL link to the song")

        def __str__(self):
            return self.name
