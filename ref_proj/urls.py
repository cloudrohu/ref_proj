from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include
from profiles.views import *
from ref_proj.views import main_view , signup_view
from main.views import home_view,ABOUT_US,CONTCAT,PAGE_NOTFOUND
from profiles.views import my_recommendations_view, my_account_view,DO_LOGIN

urlpatterns = [ 

    path('admin/', admin.site.urls),
    
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup-view'),
    path('my-account/', my_account_view, name='my-account'),
    path('profile/', my_recommendations_view, name='profile'),



    path('about', ABOUT_US,name='about'),
    path('contact', CONTCAT,name='contact'),
    path('404', PAGE_NOTFOUND,name='404'),


    # AC
    path('do_login', DO_LOGIN,name='do_login'),


    path('<str:ref_code>/', main_view, name='main-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
