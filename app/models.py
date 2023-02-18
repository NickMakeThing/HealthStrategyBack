from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Post(models.Model):
    title = models.SlugField(unique=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.SlugField(unique=True, max_length=255)
    main_image = models.SlugField(unique=True, max_length=255)
    content = ArrayField(models.TextField())