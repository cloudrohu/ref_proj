from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include
from product.views import *
from ref_proj.views import main_view , signup_view
from mls.views import GURUKUL,SINGLE_COURS,filter_data,SEARCH_COURSE,COURSE_DETAILS
from main.views import home_view,ABOUT_US,CONTCAT,PAGE_NOTFOUND
from profiles.views import my_recommendations_view, my_account_view,REGISTER,DO_LOGIN,Profile_Update,PROFILE

urlpatterns = [ 

    path('admin/', admin.site.urls),    
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



    path('', home_view, name='home'),

    path('signup/', signup_view, name='signup-view'),
    path('my-account/', my_account_view, name='my-account'),
    path('profile/', my_recommendations_view, name='profile'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', REGISTER,name='register'),
    path('do_login', DO_LOGIN,name='do_login'),
    path('accounts/profile', PROFILE,name='update-email'),
    path('accounts/profile_update', Profile_Update,name='profile_update'),




    path('about/', ABOUT_US,name='about'),
    path('contact', CONTCAT,name='contact'),
    path('404', PAGE_NOTFOUND,name='404'),

    path('gurukul', GURUKUL,name='gurukul'),
    path('coureses', SINGLE_COURS,name='coureses'),
    path('courese/filter-data',filter_data,name="filter-data"),
    path('search',SEARCH_COURSE,name='search_course'),    
    path('course/<slug:slug>',COURSE_DETAILS,name='course_details'),

    path('product', PRODUCT, name='product'),

    path('product_details/<slug:slug>', product_details, name='product_details'),
    path('product/filter-data',filter_data,name="filter-data"),


    path('<str:ref_code>/', main_view, name='main-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
