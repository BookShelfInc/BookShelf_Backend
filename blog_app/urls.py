from django.conf.urls import url

from .views import get_all_posts, get_user_posts, create_post, get_post_info, create_comment, \
    create_upvote, is_liked

urlpatterns = [
    url(r'^posts/all/$', get_all_posts),
    url(r'^posts/user/$', get_user_posts),
    url(r'^post/create/$', create_post),
    url(r'^post/(?P<pk>[0-9]+)/$', get_post_info),
    url(r'^post/comments/create/$', create_comment),
    url(r'^post/upvote/create/$', create_upvote),
    url(r'^post/upvote/isliked/(?P<pk>[0-9]+)/$', is_liked),
]