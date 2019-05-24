from django.contrib.admin import site
from blog.models import Article

site.register(Article)