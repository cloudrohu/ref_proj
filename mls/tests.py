
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from time import time
from models import *

# Create your tests here.
#-------------------------------------------------------------------------------------------------------------
def SINGLE_COURS(request):
    cotegory = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    level = Level.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()


    context = {
        'cotegory' : cotegory,
        'course' : course,
        'level' : level,
        'FreeCourse_count': FreeCourse_count,
        'PaidCourse_count': PaidCourse_count,
    }
    return render(request, 'Main/single_course.html',context)



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
        'cotegory':cotegory,
        'time_duration':time_duration,
        'enroll_status':enroll_status
    }
    return render(request,'course/course_details.html', context)

#--------------------------------------------------------------------------------------------------

def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
    }
    return render(request,'search/search.html',context)



#----------------------------------------------------------------------------------------------------------