from django.shortcuts import render
from django.http import HttpResponse

def displayBooks(request):
    return HttpResponse('hello i am a god')

def home(request):
    return HttpResponse('this is home')

# Create your views here.
