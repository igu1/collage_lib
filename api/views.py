from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.core.mail import send_mail
from core_library.settings import EMAIL_HOST_USER

class Cron(APIView):
    def get(self, request):
        subject = 'Cron Job Status'
        message = 'Cron job is working!'
        from_email = EMAIL_HOST_USER
        recipient_list = ['eesaard@gmail.com']  # Replace with the email address of the recipient

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return Response({
            'message': "Hello World",
        }, status=200)