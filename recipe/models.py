from django.db import models

class Recipe(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  body = models.TextField()
  
  def __unicode__(self):
    return self.title
