from django.conf.urls import url

from .views import getWishlist, getQuotes, getBookshelf

urlpatterns = [
    url(r'^wishlist/$', getWishlist),
    url(r'^quotes/$', getQuotes),
    url(r'^bookshelf/$', getBookshelf),
]