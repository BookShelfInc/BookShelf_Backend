from django.db import models

from auth_app.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=256, blank=False, null=False)
    last_name = models.CharField(max_length=256, blank=False, null=False)
    avatar = models.ImageField(upload_to='Images/', blank=False, null=False)
    biography = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='Images/', blank=False, null=False)
    genre = models.CharField(max_length=256, blank=False, null=False)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

class Rate(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    rating_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=rating_choices, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.book.title
