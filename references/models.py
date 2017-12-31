from django.db import models
import json

# Create your models here.
class Reference(models.Model):

    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    tags = models.TextField()

    def setTags(self, tags):
        self.tags = json.dumps(tags)

    def getTags(self):
        return json.loads(self.tags)