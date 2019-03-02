from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length = 255)
    date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:10]