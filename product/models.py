from django.db import models
from django.utils.html import mark_safe

from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField



# Create your models here.


# Brand
class Brand(models.Model):
    Brand_Name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image")

    class Meta:
        verbose_name_plural='2. Brands'

    def __str__(self):
        return self.Brand_Name
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

DISCOUNT_DEAL = (
        ('Hot Deals','Hot Deals'),
        ('New Arraivels','New Arraivels'),     
    )
#Slider---------------------------------------------------------------------------------------------------------------------------------------------------

class Slider(models.Model):
    image = models.ImageField(upload_to='image')
    Sale = models.IntegerField()
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    Discount_deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='1. Slider'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.Discount_deal
    
#Banner---------------------------------------------------------------------------------------------------------------------------------------------------

class Banner(models.Model):
    image = models.ImageField(upload_to='image')
    Sale = models.IntegerField()
    Quote = models.CharField(max_length=250,null=True)
    Discount_deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='3. Banner'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.Quote
    
#Category---------------------------------------------------------------------------------------------------------------------------------------------------


class Category(models.Model):
    image = models.ImageField(upload_to='image')
    category_name = models.CharField(max_length=250,null=True)
    slug = models.SlugField(unique=True , null=True , blank=True)
    class Meta:
        verbose_name_plural='5. Category'


    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category ,self).save(*args , **kwargs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.category_name
    

class Sub_Category(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=250,null=True)    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True , null=True , blank=True)


    class Meta:
        verbose_name_plural='6. Sub_Category'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name + " -- " + self.category.name    




#Slider---------------------------------------------------------------------------------------------------------------------------------------------------

class Section(models.Model):
    name = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='7. Section'

    def __str__(self):
        return self.name 
    
class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name_plural='8. Tag'

    def __str__(self):
        return self.name 
    
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='11. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title
    
class Product(models.Model):   
    category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)	
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    product_name = models.CharField(max_length=250,null=True)
    total_quantity = models.IntegerField()
    total_availability = models.IntegerField()    
    sort_description = RichTextField()    
    description = RichTextField()
    model_name = models.CharField(max_length=100)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=500,null=True,blank=True)


    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_details",kwargs={'slug':self.slug})

    class Meta:
        db_table = "app_Product"
    

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_reciver, Product)


class More_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    more_image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='9. Image'

    def __str__(self):
        return self.name

class Additional_information(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    speciation = models.CharField(max_length=250,null=True)    
    details = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name_plural='10. Additional information'
