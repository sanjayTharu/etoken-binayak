from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('home/',login_required(views.home),name='home'),    
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_page,name='logout'),
]