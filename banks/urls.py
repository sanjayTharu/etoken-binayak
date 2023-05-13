from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('bank/',login_required(views.bank),name='bank'),
    path('adbl/',login_required(views.adbl),name='adbl'),
    path('nbb/',login_required(views.nbb),name='nbb'),
    path('rbb/',login_required(views.rbb),name='rbb'),
    path('sbl/',login_required(views.sbl),name='sbl'),
]