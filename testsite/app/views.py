from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated, ) # can also pass IsAdmin User for permission Purpose
    print(permission_classes)
    
    def get(self, request):
        data = {'message': "Hola Amigos"}
        return Response(data)
