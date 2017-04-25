from django.conf.urls import url

from .views import get_books, book_detail, rate_book, review_book, getBookReviews, iswrote_review, \
    get_authors, get_author_info

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', book_detail),
    url(r'^all/$', get_books),
    url(r'^rate/$', rate_book),
    url(r'^review/$', review_book),
    url(r'^review/(?P<pk>[0-9]+)/$', getBookReviews),
    url(r'^isreview/', iswrote_review),
    url(r'^author/all/', get_authors),
    url(r'^author/(?P<pk>[0-9]+)/', get_author_info),
]