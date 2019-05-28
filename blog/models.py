from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.title, self.published_date)

class Topic(models.Model):
  name = models.CharField(max_length=255)
  topic = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topics')

  def _str_(self):
    return f'{self.name}'