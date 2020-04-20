from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class grinderuser(User):
    def __str__(self):
        return self.username

class Playlist(models.Model):
    Playlist_id = models.AutoField(primary_key=True)#Django gives each model this field by default
    Playlist_title = models.CharField(max_length = 200, help_text = "Enter a name for your playlist")
    date_created = models.DateField(auto_now_add = True)
    #grinderuser = models.ForeignKey(grinderuser, on_delete = models.CASCADE, null=True, related_name = 'playlist')
    def __str__(self):
        return self.Playlist_title

class song(models.Model):
    song_id = models.AutoField(primary_key=True)#Django gives each model this field by default
    song_title = models.CharField(max_length = 300)
    #playlists = models.ForeginKey(Playlist, on_delete = models.CASCADE)#, null = True)
    stream_source = models.CharField(max_length = 1000, help_text = "Copy and paste the URL link to the song")
    def __str__(self):
        return self.song_title
