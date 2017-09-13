# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.shortcuts import render, HttpResponse
from .models import Form


# Create your views here.

# index page
def index(req):
    if req.method == "POST":
        _name = req.POST['name']
        _email = req.POST['email']
        _subject = req.POST['subject']
        _message = req.POST['message']
        Form.objects.create(name=_name, email=_email, subject=_subject, message=_message)
        print('sada')
        mailIt(req,_subject,_message, _email, ['lazure.net@gmail.com'])
    return render(req,'contact.html')


def mailIt(req,subject,message,sender,accepter):
    if subject and message and sender:
        try:
            send_mail(subject, 'somebody filled form with email '+sender+' -> '+ message, settings.EMAIL_HOST_USER, accepter)
            messages.success(req, "completed successfully")
        except BadHeaderError:
            pass
