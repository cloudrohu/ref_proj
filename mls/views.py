from multiprocessing import context
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from time import time
from .models import *
from main.models import *

import razorpay
from ref_proj.settings import *





# Create your views here.
def BASE(request):
    return render(request,'base.html', )

def GURUKUL(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    cotegory = Categories.objects.all().order_by('id')[0:7]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'cotegory' : cotegory,
        'course' : course,
        'header' : header,
        'footer' : footer,
    }
    return render(request,'mls/Main/home.html', context)


#-------------------------------------------------------------------------------------------------------------
def SINGLE_COURS(request):

    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    cotegory = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    level = Level.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()


    context = {
        'header' : header,
        'footer' : footer,

        'cotegory' : cotegory,
        'course' : course,
        'level' : level,
        'FreeCourse_count': FreeCourse_count,
        'PaidCourse_count': PaidCourse_count,
    }
    return render(request, 'mls/Main/single_course.html',context)



#-----------------------------------------------------------------------------------------------------
def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    
    


    if price == ['pricefree']:
       course = Course.objects.filter(price=0)

    elif price == ['pricepaid']:
       course = Course.objects.filter(price__gte=1)
       
    elif price == ['priceall']:
       course = Course.objects.all()


    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')

    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')

    else:
       course = Course.objects.all().order_by('-id')


    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})

#-----------------------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')

def COURSE_DETAILS(request,slug):
    cotegory = Categories.get_all_category(Categories)
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum=Sum('time_duration'))

    course_id = Course.objects.get(slug = slug)   

    try:
        enroll_status = UserCourse.objects.get(user=request.user, course=course_id)
    except UserCourse.DoesNotExist:
        enroll_status = None

    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course':course,
        'header':header,
        'footer':footer,
        'cotegory':cotegory,
        'time_duration':time_duration,
        'enroll_status':enroll_status
    }
    return render(request,'course/course_details.html', context)

#--------------------------------------------------------------------------------------------------

def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    context = {
        'course':course,
        'header': header,        
        'footer': footer,
    }
    return render(request,'search/search.html',context)



#----------------------------------------------------------------------------------------------------------
def PAGE_NOTFOUND(request):
    cotegory = Categories.objects.all()
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    context = {        
        'cotegory' : cotegory,       
        'header' : header,       
        'footer' : footer,       
        
    }
    return render(request, 'error/error404.html',context)


#-------------------------------------------------------------------------------------------------------------
def CHECKOUT(request,slug):
    cotegory = Categories.objects.all() 
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    
    if  course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course,
        )
        course.save()
        messages.success(request,'Course are successfully Enrolles !')
        return redirect('my_course')
    
    elif action == 'create_payment':
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            city = request.POST.get('city')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_comments = request.POST.get('order_comments')

            amount = course.price * 100
            currency = "INR"

            notes = {
                "Name": first_name,
                "last_name": last_name,
                "country": country,
                "address_1": address_1,
                "address_2": address_2,
                "city": city,
                "postcode": postcode,
                "phone": phone,
                "email": email,
                "order_comments": order_comments,

            }
            receipt = " BCS {int(time())}"
            order = client.order.create(
                {
                    'receipt': receipt,
                    'notes': notes,
                    'amount': amount,
                    'currency': currency,

                }
            )
            payment = Payment(
                course=course,
                use=request.user,
                order_id=order.get('id')
            )
            payment.save()



    context = {        
        'cotegory' : cotegory,  
        'course'  : course,    
        'order'  : order,    
        'header'  : header,    
        'footer'  : footer,    
        
    }
    return render(request, 'checkout/checkout.html',context)
#--------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def MY_COURSE(request):
    cotegory = Categories.objects.all()
    course = UserCourse.objects.filter(user = request.user)
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    
    
    context = {        
        'cotegory' : cotegory,
        'course' : course,       
        'header' : header,       
        'footer' : footer,       
        
    }
    return render(request, 'course/my_course.html',context)
    
#-------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')

def WATCH_COURSE(request,slug):
    course = Course.objects.filter(slug = slug)  
    lecture =  request.GET.get('lecture')
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    
    
    video = Video.objects.get(id = lecture)
        

    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {       
        'course' : course,
        'video'  : video,
        'footer'  : footer,
        'header'  : header,
        
        }
        
    return render(request, 'course/watch-course.html',context)

