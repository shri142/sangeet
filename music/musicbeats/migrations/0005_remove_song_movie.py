# Generated by Django 4.0.3 on 2022-07-21 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0004_song_movie_alter_song_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='movie',
        ),
    ]