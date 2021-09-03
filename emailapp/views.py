from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def email(request):
    if request.method ==  "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        data= {
            'name':name,
            'email':email,
            'message':message,
            'subject':subject,
        }
        message = '''
        New message:{}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message, '',['kavyakishor729@gmail.com'])
        return HttpResponse('thank you for the message we will touch you soon')


    return render(request,'email.html')
