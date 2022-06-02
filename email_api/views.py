from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def Accept(request):
    subject = "Congratulations!!!(Title of mail)"
    msg = " First and foremost, let me begin by thanking you for applying to backend developer intern position in finnove technologies.This mail is to let you know you are one of the selected few who have been selected for this position and you will hear from us shortly on further steps."
    to = "restapi94@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfully."
    else:
        msg = "Mail Sending Failed."
    return HttpResponse(msg)

def Reject(request):
    subject = "Greetings from Finnove Tech."
    msg = "Thank you for your interest in the Graphic Designer position at Khojdeu.com in Kathmandu, Bāgmatī, Nepal. Unfortunately, we will not be moving forward with your application, but we appreciate your time and interest in Khojdeu.com. Regards:Khojdeu.com "
    

    to = "restapi94@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfully."
    else:
        msg = "Mail Sending Failed."
    return HttpResponse(msg)