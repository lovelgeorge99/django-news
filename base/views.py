from django.shortcuts import render
from newsapi import NewsApiClient
from .news import context
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage




def home(request):
    return render(request,'base/index.html',context)

def email_sent(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['comment']
        
        ctx={
            'user': name,
            'email':email,
            'comment':comment
        }
        message=get_template('base/email_template.html').render(ctx)
        msg=EmailMessage(
            'FROM NEWS',
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        msg.content_subtype='html'
        msg.send()

        #send_mail('From News : '+' '+name,comment,email,[settings.EMAIL_HOST_USER,],fail_silently=False,)
        return render(request,'base/email_sent.html')
