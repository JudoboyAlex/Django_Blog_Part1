from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')  

    def __str__(self):
        return "{} - {}".format(self.title, self.published_date)

class Topic(models.Model):
  name = models.CharField(max_length=255)
  topic = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topics')

  def _str_(self):
    return f'{self.name}'

class Comment(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  message = models.TextField()
  blog_comment = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  
