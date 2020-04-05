from django.contrib import admin
from .models import grinderuser, Playlist, song

# Register your models here.
admin.site.register(grinderuser)
admin.site.register(Playlist)
admin.site.register(song)
