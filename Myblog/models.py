from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Author (models.Model):
    id = models.BigAutoField (primary_key = True)
    profile = models.CharField(max_length = 200)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 100, unique = True)
    content = models.TextField()
    comments = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
