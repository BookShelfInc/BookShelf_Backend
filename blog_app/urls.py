from django.conf.urls import url

from .views import get_all_posts, get_user_posts, create_post, get_comments, create_comment, create_upvote

urlpatterns = [
    url(r'^posts/all/$', get_all_posts),
    url(r'^posts/user/$', get_user_posts),
    url(r'^posts/create/$', create_post),
    url(r'^post/comments/(?P<pk>[0-9]+)/$', get_comments),
    url(r'^post/comments/create/$', create_comment),
    url(r'^post/upvote/create/$', create_upvote),
]