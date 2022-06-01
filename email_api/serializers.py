from rest_framework import serializers
from .models import Consult
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from email_api.utils import Util
from django.forms import ValidationError

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = ('id', 'name', 'position', 'group', 'email', 'phone', 'describe', 'file', 'create_date')


# user password reset email send ...  serializer
class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    #validate email_exist or not
    def validate(self, attrs):
        email = attrs.get('email')
        if Consult.objects.filter(email=email).exists():
            user = Consult.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            # print('Encoded UID', uid)
            text = 'this is a hello world text'+uid+'/'
            print('Password Reset Link', text)
            #send email
            body = 'Hello guys.... this text for you'+text
            data={
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationError('You are not a registered User')