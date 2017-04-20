from django.conf.urls import url

from .views import get_books, book_detail, rate_book, review_book

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', book_detail),
    url(r'^books/$', get_books),
    url(r'^rate/$', rate_book),
    url(r'^review/$', review_book)
]