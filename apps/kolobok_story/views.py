from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'kolobok_story/index.html')
