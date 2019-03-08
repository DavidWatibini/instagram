from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insta_index(request):

    return render(request,'index.html')

def home_index(request):

    return render(request,'home.html')
