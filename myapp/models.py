from django.db import models


class Hymn(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=400)
    content = models.TextField()

    def __str__(self):
        return self.title
