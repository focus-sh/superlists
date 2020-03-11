
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout
from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']

    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'alert_weshare@sina.com',
        [email],
        fail_silently=False,
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(request.GET.get('token'))
    if user is not None:
        auth.login(request, user)

    return redirect('/')


def logout(request):
    django_logout(request)
    return redirect('/')
