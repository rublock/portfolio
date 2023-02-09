from django.db import models
from django.forms import JSONField

class DataBase(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=9999, verbose_name='Description')
    image = models.ImageField(upload_to='static/img', verbose_name='Image')
    url = models.URLField(blank=True, verbose_name='Url')
    tech = models.JSONField()

    def __str__(self):
        return self.title
