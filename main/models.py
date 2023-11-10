from django.db import models
from django.utils.html import mark_safe

from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField
# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)    
    title2 = models.CharField(max_length=100)    
    discription = models.TextField()
    link = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='1. Slider'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title