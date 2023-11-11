from django.shortcuts import render
from .models import *
# Create your views here.


def home_view(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    founder_member = Founder_Member.objects.all().order_by('-id')[0:15]
    achiever = Achiever.objects.all().order_by('-id')[0:50]


    context = {
        'sliders': sliders,        
        'founder_member': founder_member,        
        'achiever': achiever,        
    }
    return render(request, 'main/home.html', context)


def LMS_HOME(request):
    return render(request,'mls/home.html', )

def ABOUT_US(request):
    return render(request,'mls/Main/about_us.html', )



def CONTCAT(request):
    return render(request,'mls/Main/contact_us.html', )



def PAGE_NOTFOUND(request):
    return render(request,'mls/base.html', )