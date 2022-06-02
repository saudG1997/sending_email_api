from rest_framework import serializers
from email_api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email']