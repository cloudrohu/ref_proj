from django.contrib import admin
from .models import *
# Register your models here.



class SliderAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','title','title2','discription','link')
admin.site.register(Slider,SliderAdmin)


class Founder_MemberAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','name','title','discription',)
admin.site.register(Founder_Member,Founder_MemberAdmin)


class AchieverAdmin(admin.ModelAdmin):    
    list_display = ('id','image_tag','name','title','discription',)
admin.site.register(Achiever,AchieverAdmin)



class Social_LinkAdmin(admin.ModelAdmin):    
    list_display = ('id','facebook','youtube','Instagram','Snapchat','Twitter','Pinterest','Reddit','LinkedIn','Threads')
admin.site.register(Social_Link,Social_LinkAdmin)



class FaqAdmin(admin.ModelAdmin):    
    list_display = ('id','question','answers')
    list_editable = ('question','answers')


class AboutAdmin(admin.ModelAdmin):    
    list_display = ('id','main_title','experience','title','sub_title','how_to_work','mission','vision','values')


class HeaderAdmin(admin.ModelAdmin):    
    list_display = ('id','color','number','contant_1','contant_2','contant_3')

class FooterAdmin(admin.ModelAdmin):    
    list_display = ('id','color','facebook','youtube','whatsApp','instagram','telegram','pinterest','twitter','linkedIn','copyright')

class MetaAdmin(admin.ModelAdmin):    
    list_display = ('id','title','keyword','discriptaion',)

class ContactAdmin(admin.ModelAdmin):    
    list_display = ('id','where_we_are','form_name','address','number','email_id','location_map')

class EventAdmin(admin.ModelAdmin):    
    list_display = ('id','name','event','description')


class BannerAdmin(admin.ModelAdmin):    
    list_display = ('id','image','name','line_1','line_2')

class AboutAdmin(admin.ModelAdmin):    
    list_display = ('id','image','main_title','experience','title','sub_title','how_to_work','mission','vision','values')


admin.site.register(Contact,ContactAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Banner,BannerAdmin)

admin.site.register(Meta,MetaAdmin)
admin.site.register(Header,HeaderAdmin)
admin.site.register(Footer,FooterAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Companylogo)