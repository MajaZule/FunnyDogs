from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(blank=True, default=datetime.datetime.now)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=3000)
    time_stamp = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

class Comment(models.Model):
	content = models.CharField(max_length=1000)
	time_stamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

class Tag(models.Model):
	name = models.CharField(max_length=100)

class TagEntry(models.Model):
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# extend models
# add comment

