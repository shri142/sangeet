from django.db import models

# Create your models here.

class Song(models.Model):
    # song_id = models.AutoField(primary_key=True ) # unable to makemigrations and migrate //solve it after
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents')
    song = models.FileField(upload_to='documents')
    # movie = models.CharField(max_length=150, default="None")

def __str__(self):
    return self.name