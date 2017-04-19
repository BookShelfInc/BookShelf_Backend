from django.conf.urls import url

from .views import getBooks, getRatings

urlpatterns = [
    url(r'^books/$', getBooks),
    url(r'^ratings/$', getRatings),
]