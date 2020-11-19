from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    pass
    access_token = models.CharField(blank=True, default= None, max_length = 300, null=True)
    refresh_token = models.CharField(blank=True, default= None, max_length = 300, null=True)
    expires_in = models.IntegerField(blank=True, default= None, null=True)

    def __str__(self):
        return self.username
    # A method to flag when token needs to be refreshed 

class Playlist (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    collaborative=models.BooleanField()
    description = models.CharField(max_length=255, null=True)
    external_urls = models.CharField(max_length=255, null=True)
    followers = models.CharField(max_length=255, null=True)
    href = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    public = models.BooleanField()
    snapshot_id = models.CharField(max_length=255, null=True)
    tracks = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    uri = models.CharField(max_length=255, null=True)


class Track (models.Model):
    album = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)
    artist = JSONField(null=True)
    available_markets = models.CharField(max_length=255 ,null=True)
    disc_number = models.IntegerField(null=True)
    duration_ms = models.IntegerField(null=True)
    explicit = models.BooleanField(null=True)
    external_ids= models.CharField(max_length=255, null=True)
    external_urls = models.CharField(max_length=255, null=True)
    href = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    is_playable = models.BooleanField(null=True)
    name = models.CharField(max_length=255,null=True)
    popularity = models.IntegerField(null=True)
    preview_url = models.CharField(max_length=255,null=True)
    track_number = models.IntegerField(null=True)
    type = models.CharField(max_length=255, null=True)
    uri = models.CharField(max_length=255, null=True)
    is_local = models.BooleanField(null=True)

class audio_features_object(models.Model):
    acousticness = models.FloatField()
    analysis_url = models.CharField(max_length=255 ,null=True)
    danceability = models.FloatField()
    duration_ms = models.IntegerField()
    energy = models.FloatField()
    id = models.CharField(max_length=255 , primary_key=True)
    instrumentalness = models.FloatField()
    key = models.IntegerField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.IntegerField()
    track_href = models.CharField(max_length=255 ,null=True)
    type = models.CharField(max_length=255 ,null=True)
    uri = models.CharField(max_length=255 ,null=True)
    valence = models.FloatField()

class recommendations_seed_object(models.Model):
    afterFilteringSize = models.IntegerField()
    afterRelinkingSize = models.IntegerField()
    href = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    initialPoolSize = models.IntegerField()
    type = models.CharField(max_length=255)

class recommendations_object():
    seeds = ArrayField(JSONField(),primary_key=True)
    tracks = ArrayField(JSONField())
