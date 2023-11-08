"""
URL configuration for ref_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from profiles.views import *
from ref_proj.views import main_view , signup_view
from profiles.views import my_recommendations_view,my_account_view,home_view

urlpatterns = [

    
    path('admin/', admin.site.urls),
    
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup-view'),
    path('my-account/', my_account_view, name='my-account'),
    path('profile/', my_recommendations_view, name='profile'),

    path('<str:ref_code>/', main_view, name='main-view'),
]
