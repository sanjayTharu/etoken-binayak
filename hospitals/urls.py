from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns=[
    path('hospital/',login_required(views.hospital),name='hospital'),
    # path('bpk/',views.BpkView.as_view(),name='bpk'),
    # path('bharatpur/',views.BharatpurView.as_view(),name='bharatpur'),
    path('bharatpur/',login_required(views.bharatpur),name='bharatpur'),
    path('bpk/',login_required(views.bpk),name='bpk'),
]
