from django.conf.urls import url

from .views import getWishlist, getQuotes, getBookshelf, addBookToWishlist, addQuote, \
    addBookToBookshelf, createBookshelf

urlpatterns = [
    url(r'^wishlist/all/$', getWishlist),
    url(r'^wishlist/add/$', addBookToWishlist),
    url(r'^quotes/all/$', getQuotes),
    url(r'^quotes/add/$', addQuote),
    url(r'^bookshelf/all/$', getBookshelf),
    url(r'^bookshelf/add/$', addBookToBookshelf),
    url(r'^bookshelf/create/$', createBookshelf),
]