from django.contrib import admin
from .models import Slider
# Register your models here.



class SliderAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','title','title2','discription','link')
admin.site.register(Slider,SliderAdmin)