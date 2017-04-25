from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import register, getInfo

urlpatterns = [
    url(r'^register/', register),
    url(r'^login/', obtain_jwt_token),
    url(r'^info/$', getInfo),
]