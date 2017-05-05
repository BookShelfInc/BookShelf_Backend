from django.conf.urls import url

from .views import get_all_posts, get_user_posts, create_post, get_post_info, create_comment, \
    create_upvote, is_liked, delete_comment, delete_post

urlpatterns = [
    url(r'^post/all/$', get_all_posts),
    url(r'^post/user/(?P<pk>[0-9]+)/$', get_user_posts),
    url(r'^post/delete/(?P<pk>[0-9]+)/$', delete_post),
    url(r'^post/create/$', create_post),
    url(r'^post/(?P<pk>[0-9]+)/$', get_post_info),
    url(r'^post/comment/create/$', create_comment),
    url(r'^post/comment/delete/(?P<pk>[0-9]+)/$', delete_comment),
    url(r'^post/upvote/create/$', create_upvote),
    url(r'^post/upvote/isliked/(?P<pk>[0-9]+)/$', is_liked),
]