from django.conf.urls import url

from .views import get_all_ads, create_bazaar_ad, delete_bazaar_ad

urlpatterns = [
    url(r'^all/$', get_all_ads),
    url(r'^create/$', create_bazaar_ad),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete_bazaar_ad),
]