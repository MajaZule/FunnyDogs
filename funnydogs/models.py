from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(blank=True, default=datetime.datetime.now)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    time_stamp = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
