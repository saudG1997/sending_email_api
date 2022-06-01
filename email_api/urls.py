from email_api import views
from email_api.views import SendEmailView
from django.urls import path
urlpatterns = [
    path('sendemail/', SendEmailView.as_view(), name='email'),
]