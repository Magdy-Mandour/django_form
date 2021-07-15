from django.shortcuts import redirect, render
from .forms import contactform
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse


def homepage(request):
    return render(request=request, template_name='main/home.html')


def contact(request):
    if request.method == 'post':        
       form = contactform(request.POST)
       if form.is_valid():
           subject = 'website Inquery'
           body = {
               'first_name': form.cleaned_data['first_name'],
               'last_name': form.cleaned_data['last_name'],
               'email': form.cleaned_data['email_adress'],
               'message': form.cleaned_data['message'],
           }
           message = '\n'.join(body.values())
                # try:
                #     send_mail(subject, message, 'admin@gmail.com',['admin@gmail.com'])
                # except BadHeaderError:
                #     retrun HttpResponse('invalidv header')
    form = contactform()
    return render(request, 'main/contact.html', {'form':form})

