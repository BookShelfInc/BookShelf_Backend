from django.conf.urls import url

from .views import getBooks

urlpatterns = [
    url(r'^books/$', getBooks),
]