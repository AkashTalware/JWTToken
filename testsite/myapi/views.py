from django.shortcuts import render
from .serializers import HeroSerializer
from .models import Hero
import requests
from rest_framework import viewsets
from django.http import JsonResponse
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('keyword')
    serializer_class = HeroSerializer

def getDetails(request):

    print("@@@@@@@@@@@@@@@@")
    print(request.method)
    print("***************")
    details = {'name': 'Chandan', 'address': 'Pune'}
    return JsonResponse(details)
