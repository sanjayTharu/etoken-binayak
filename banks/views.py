from django.shortcuts import render
from django.core.mail import send_mail
from .models import Token
import uuid
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def bank(request):
    return render(request,'banks/bank.html')
@login_required
def adbl(request):
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

        return render(request, 'banks/adbbl.html', {'token_number': token_number})
    return render(request,'banks/adbl.html')
@login_required
def nbb(request):
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

        return render(request, 'banks/nbb.html', {'token_number': token_number})
    return render(request,'banks/nbb.html')
@login_required
def rbb(request):
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

        return render(request, 'banks/rbb.html', {'token_number': token_number})
    return render(request,'banks/rbb.html')
@login_required
def sbl(request):
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

        return render(request, 'banks/sbl.html', {'token_number': token_number})
    return render(request,'banks/sbl.html')