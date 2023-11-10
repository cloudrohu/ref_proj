from django.contrib import admin
from .models import *

# Register your models here.

class BrandAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','Brand_Name')


admin.site.register(Brand,BrandAdmin)

class SliderAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','Sale','Brand','Discount_deal','Discount','Link')
admin.site.register(Slider,SliderAdmin)


class BannerAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','Sale','Discount_deal','Discount','Link')
admin.site.register(Banner,BannerAdmin)

#Category---------------------------------------------------------------------------------------------------------------------------------------------------


class CategoryAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','category_name')
    
    search_fields = ['category_name']
    list_per_page = 20 
admin.site.register(Category,CategoryAdmin)

class Sub_CategoryAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','name','category','slug')

    list_filter = ['category',]
    search_fields = ['name']
    list_per_page = 20 
admin.site.register(Sub_Category,Sub_CategoryAdmin)

# END Category---------------------------------------------------------------------------------------------------------------------------------------------------

class SectionAdmin(admin.ModelAdmin):    
    list_display = ('id','name',)
admin.site.register(Section,SectionAdmin)


admin.site.register(Additional_information,)
admin.site.register(More_Image)
admin.site.register(Tag)

class Product_images(admin.TabularInline):
    model = More_Image

class Additional_information(admin.TabularInline):
    model = Additional_information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_images,Additional_information)   
    list_display = ('id','image_tag','product_name','category','brand','section','color','total_quantity','total_availability','model_name','price','discount','slug')
    list_filter = ['category','brand','section','total_quantity','total_availability','model_name','price','discount','tags',]
    search_fields = ['id','product_name','category','brand','section','total_quantity','total_availability','model_name','price','discount','tags','slug']
    list_per_page = 20 
admin.site.register(Product,Product_Admin)

class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)




