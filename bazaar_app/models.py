from django.db import models

from book_app.models import Book
from auth_app.models import User

class BazaarBook(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    price = models.IntegerField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.user.username + ' ' + self.book.title