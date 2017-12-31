from django.db import models
import json

# Create your models here.
class Reference(models.Model):

    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    tags = models.TextField()
    pub_date = models.DateTimeField()