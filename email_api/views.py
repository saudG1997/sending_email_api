from rest_framework import viewsets
from .models import Consult
from .serializers import ConsultSerializer, SendEmailSerializer
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


# user password reset email send ...  views
class SendEmailView(APIView):
    def post(self, request, format=None):
        serializer = SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Send your message. Please check your Email'}, status=status.HTTP_200_OK)