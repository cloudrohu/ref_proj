from django.shortcuts import render
from .models import *
# Create your views here.


def home_view(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    founder_member = Founder_Member.objects.all().order_by('-id')[0:15]
    achiever = Achiever.objects.all().order_by('-id')[0:15]
    about = About.objects.all().order_by('-id')[0:1]
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]


    context = {
        'sliders': sliders,        
        'founder_member': founder_member,        
        'achiever': achiever,        
        'about': about,        
        'header': header,        
        'footer': footer,        
    }
    return render(request, 'main/home.html', context)

def ABOUT_US(request):

    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    about = About.objects.all().order_by('-id')[0:1]



    context = {               
        'header': header,        
        'footer': footer,        
        'about': about,        
    }
    
    return render(request,'mls/Main/about_us.html',context )



def CONTCAT(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    contact = Contact.objects.all().order_by('-id')[0:1]


    context = {               
        'header': header,        
        'footer': footer,        
        'contact': contact,        
    }
    return render(request,'mls/Main/contact_us.html',context )



def PAGE_NOTFOUND(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]


    context = {               
        'header': header,        
        'footer': footer,        
    }
    return render(request,'mls/base.html',context )