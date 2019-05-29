from django.contrib.admin import site
from blog.models import Article, Comment

site.register(Article)
site.register(Comment)