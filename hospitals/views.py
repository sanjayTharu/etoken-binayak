from django.shortcuts import render
from django.views import View
from .models import Token
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def hospital(request):
    return render(request,'hospitals/hospital.html')

@login_required
def bharatpur(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')
        token = Token.objects.create(
            date=date,
            name=name,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            token_number=uuid.uuid4()
        )

        token_number = token.token_number
        send_mail(
            'Token Confirmation',
            f'Your token number is: {token_number}',
            'sender@example.com',  # Replace with your email address
            [email],
            fail_silently=False,
        )

        return render(request, 'hospitals/bharatpur.html', {'token_number': token_number})

    return render(request,'hospitals/bharatpur.html')
@login_required
def bpk(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')

        token = Token.objects.create(
            date=date,
            name=name,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            token_number=uuid.uuid4()
        )

        token_number = token.token_number

        send_mail(
            'Token Confirmation',
            f'Your token number is: {token_number}',
            'sender@example.com',  # Replace with your email address
            [email],
            fail_silently=False,
        )

        return render(request, 'hospitals/bpk.html', {'token_number': token_number})

    return render(request,'hospitals/bpk.html')
