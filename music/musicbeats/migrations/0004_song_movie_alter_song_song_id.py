# Generated by Django 4.0.3 on 2022-07-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0003_alter_song_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
