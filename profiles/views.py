from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='home')
def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommened_profiles

    context = {
        'my_recs': my_recs

    }
    return render(request, 'dashboard/recommened.html', context)


@login_required(login_url='main-view')
def my_account_view(request):
    
    return render(request, 'dashboard/main.html', )



def DO_LOGIN(request, ):   
    
    return render(request, 'mls/registration/login.html', {})



