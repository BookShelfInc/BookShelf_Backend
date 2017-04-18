from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=256, blank=False, null=False)
    last_name = models.CharField(max_length=256, blank=False, null=False)
    avatar = models.ImageField(upload_to='Images/', blank=False, null=False)
    biography = models.TextField(blank=False, null=False)

class Book(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='Images/', blank=False, null=False)
    genre = models.CharField(max_length=256, blank=False, null=False)
    author = models.ForeignKey(Author)