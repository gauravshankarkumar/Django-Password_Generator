from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import SendMail
from .forms import UserSendMail
from django.core.mail import send_mail




# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'home':'Gaurav'})

# def about(request):
    # return render(request,'generator/about.html')

def password(request):
    return render(request,'generator/password.html')

def result(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*_'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/result.html',{'password':thepassword})

def about(request):
    if request.method == 'POST':
        mail_form = UserSendMail(request.POST)
        if mail_form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            _from = 'heavycoder.in@gmail.com'
            useremail = request.POST.get('useremail')
            mail_data = SendMail(subject=subject, message=message, useremail=useremail)
            mail_data.save()
            send_mail(
                subject,
                message,
                _from,
                [useremail],
                fail_silently=False,
            )
            mail_form = UserSendMail(request.POST)
            return render (request,'generator/contact.html', {'messages':'Mail Send Successfully','form':mail_form})
        
        else:
            mail_form = UserSendMail(request.POST)
            return render (request,'generator/contact.html', {'messages':'Mail Not Send','form':mail_form})
    else:
        mail_form = UserSendMail(request.POST)
        return render (request,'generator/contact.html', {'messages':'Write','form':mail_form})    