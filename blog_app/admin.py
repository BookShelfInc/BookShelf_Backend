from django.contrib import admin

from .models import Post, Comment, Upvote

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'id')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'id')

class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'id', 'like')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Upvote, UpvoteAdmin)