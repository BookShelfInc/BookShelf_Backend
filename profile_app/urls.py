from django.conf.urls import url

from .views import get_wishlist, get_quotes, get_bookshelf, addbookto_wishlist, delete_wishlist, add_quote, \
                    delete_quote, manage_bookshelf, create_bookshelf, delete_bookshelf

urlpatterns = [
    url(r'^wishlist/all/$', get_wishlist),
    url(r'^wishlist/add/$', addbookto_wishlist),
    url(r'^wishlist/delete/(?P<pk>[0-9]+)/$', delete_wishlist),
    url(r'^quotes/all/$', get_quotes),
    url(r'^quotes/add/$', add_quote),
    url(r'^quotes/delete/(?P<pk>[0-9]+)/$', delete_quote),
    url(r'^bookshelf/all/$', get_bookshelf),
    url(r'^bookshelf/create/$', create_bookshelf),
    url(r'^bookshelf/manage/(?P<pk>[0-9]+)/$', manage_bookshelf),
    url(r'^bookshelf/delete/(?P<pk>[0-9]+)/$', delete_bookshelf),
]