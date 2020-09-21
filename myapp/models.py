from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name.encode('utf-8')


class Hymn(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=400)
    content = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title.encode('utf-8')
