from django.db import models
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

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
    


class Founder_Member(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=100)    
    title = models.CharField(max_length=100)    
    discription = models.TextField()    

    

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    

class Achiever(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=100)    
    title = models.CharField(max_length=100)    
    discription = models.TextField()    

    

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=100)    
    title = models.CharField(max_length=100)    
    discription = models.TextField()    

    

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Social_Link(models.Model):    
    facebook = models.CharField(max_length=200)    
    youtube = models.CharField(max_length=200)    
    Instagram = models.CharField(max_length=200)    
    Snapchat = models.CharField(max_length=200)    
    Twitter = models.CharField(max_length=200)    
    Pinterest = models.CharField(max_length=200)    
    Reddit = models.CharField(max_length=200)    
    LinkedIn = models.CharField(max_length=200)    
    Threads = models.CharField(max_length=200)    

    def __str__(self):
        return self.facebook



class Companylogo(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=250,null=True)    
    def __str__(self):
        return self.name

# Events 

EVENTS = (
        ('UPCOMING','UPCOMING'),
        ('COMPLETATE','COMPLETATE'),        

    )

class Event(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=250,null=True)
    event = models.CharField(choices=EVENTS,max_length=20)
    description = models.CharField(max_length=500,null=True)       
    date = models.DateTimeField(blank=True, null=True)      
    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=250,null=True)
    answers = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.question


COLOR = (
        ('primary','primary'),
        ('secondary','secondary'),       
        ('success','success'),       
        ('danger','danger'),       
        ('warning','warning'),       
        ('info','info'),       
        ('dark','dark'),       
        ('body','body'),     
        ('white','white'),     
        ('transparent','transparent'),     
        ('light','light'),     
    )


class Header(models.Model):
    logo = models.ImageField(upload_to='image')
    color = models.CharField(choices=COLOR,max_length=100)
    number = models.CharField(max_length=12,null=True)
    contant_1 = models.CharField(max_length=250,null=True)
    contant_2 = models.CharField(max_length=250,null=True)
    contant_3 = models.CharField(max_length=250,null=True)
    
    def __str__(self):
        return self.number

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    
class Footer(models.Model):
    color = models.CharField(choices=COLOR,max_length=100)
    facebook  = models.CharField(max_length=250,null=True)
    youtube = models.CharField(max_length=250,null=True)
    whatsApp = models.CharField(max_length=250,null=True)
    instagram = models.CharField(max_length=250,null=True)
    telegram = models.CharField(max_length=250,null=True)
    pinterest = models.CharField(max_length=250,null=True)
    twitter = models.CharField(max_length=250,null=True)
    linkedIn = models.CharField(max_length=250,null=True)
    copyright = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.facebook


class Meta(models.Model):
    favicon = models.ImageField(upload_to='image')
    title = models.CharField(max_length=500,null=True)
    keyword = models.CharField(max_length=500,null=True)
    discriptaion = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.title

class Banner(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=250,null=True)
    line_1 = models.CharField(max_length=250,null=True)
    line_2 = models.CharField(max_length=250,null=True)   
    def __str__(self):
        return self.name



GENDER = (
        ('Male','Male'),
        ('Female','Female'),       
    )



class Contact(models.Model):    
    where_we_are=models.CharField(max_length=2000)
    form_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    Working_Hours=models.CharField(max_length=255)    
    number=models.CharField(max_length=255)
    email_id=models.EmailField(max_length=255)
    location_map = models.CharField(max_length=2500,null=True, blank=True)


    def __str__(self):
        return self.where_we_are
    
class About(models.Model):   
    image = models.ImageField(upload_to='image') 
    main_title=RichTextUploadingField(blank=True)

    experience=models.CharField(max_length=3)
    title=models.CharField(max_length=255)
    sub_title=models.CharField(max_length=255)    
    how_to_work=models.TextField()
    mission =models.TextField()
    vision =models.TextField()
    values =models.TextField()

    def __str__(self):
        return self.main_title
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))