# Generated by Django 2.2.10 on 2020-04-05 13:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='grinderuser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('Playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('Playlist_title', models.CharField(help_text='Enter a name for your playlist', max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=300)),
                ('stream_source', models.CharField(help_text='Copy and paste the URL link to the song', max_length=1000)),
            ],
        ),
    ]