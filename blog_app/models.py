from django.db import models

from auth_app.models import User

class Post(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='posts')

    def __str__(self):
        return self.title + ' ' + self.author.username

class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + self.post.title

class Upvote(models.Model):
    author = models.ForeignKey(User, null=False, related_name='upvotes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, related_name='upvotes', on_delete=models.CASCADE)
    like = models.BooleanField(null=False, blank=False)

    class Meta:
        unique_together = (('author', 'post'))

    def __str__(self):
        return self.author.username + ' ' + self.post.title
