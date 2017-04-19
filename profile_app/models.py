from django.db import models

from auth_app.models import User
from book_app.models import Book

class Wishlist(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    has_read = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Quote(models.Model):
    quote = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Bookshelf(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    user = models.ForeignKey(User)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name