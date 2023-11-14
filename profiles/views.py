from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

from profiles.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




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
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request,
                                     username=email,
                                     password=password)
        if user !=None:
           login(request,user)
           return redirect('my-account')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           
           return redirect('login')   





def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')

        # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request,'mls/registration/register.html')



def PROFILE(request):
    return render(request,'registration/profile.html')

def Profile_Update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')


        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
     





