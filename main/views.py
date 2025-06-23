from django.shortcuts import render
from django.http import HttpResponse

from .models import posts

# Create your views here.
def home(req):
    data=posts.objects.all().order_by('-id') 
    return render(req,'home.html',{"posts":data})