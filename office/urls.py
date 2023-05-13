from django.urls import path
from . import views


urlpatterns=[
    path('office/',views.office,name='office'),
]