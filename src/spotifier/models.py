"""Django data models for spotifier

Django Model Documentation:
https://docs.djangoproject.com/en/2.1/topics/db/models/
https://docs.djangoproject.com/en/2.1/ref/models/options/
https://docs.djangoproject.com/en/2.1/internals/contributing/writing-code/coding-style/#model-style
Django Field Reference:
https://docs.djangoproject.com/en/2.1/ref/models/fields/
https://docs.djangoproject.com/en/2.1/ref/models/fields/#charfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#manytomanyfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#textfield

"""
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    IntegerField,
)
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from playlist.models import Playlist
from track.models import Track
from grinder.models import Grinde

class Spotifier (AbstractBaseUser, PermissionsMixin):
    spotify_username = CharField(max_length=40, unique=True)
    access_token = CharField(blank=True, default= None, max_length = 300, null=True)
    refresh_token = CharField(blank=True, default= None, max_length = 300, null=True)
    expires_in = IntegerField(blank=True, default= None, null=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)

    playlists = ManyToManyField(Playlist)
    tracks = ManyToManyField(Track)
    grindes = ManyToManyField(Grinde)

    USERNAME_FIELD = 'spotify_username'

