from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from library.models import Message

class Cron(APIView):
    def get(self, request):
        # name = models.CharField(max_length=100)
        # email = models.CharField(max_length=100)
        # subject = models.CharField(max_length=100)
        # message = models.TextField()
        Message.objects.create(name="Eesa", email="eeaard@gmail.com", subject="Running Cron", message="Just Want To Let You Know That Cron Is Running")
        return Response({
        'message': "Hello World",
    }, status=200)