from django.db import router
from email_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()
#register class_name_"UserViewSet" with router
router.register('sendemail', views.UserModelViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]