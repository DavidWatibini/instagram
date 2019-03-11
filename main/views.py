from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.

#first page - signup page
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html', {"form":form})

#landing page - home page
def home_index(request):

    index_images = Image.objects.all()
    forms=CommentForm()
    comments = Comments.objects.all()
    return render(request,'home.html',locals())

def save_comment(request):
    comment = request.POST.get('comment')
    print(comment)
    image_id = request.POST.get('image_id')
    image = get_object_or_404(Image, id=image_id)
    comments = Comments.objects.create(image_id=image,comment=comment)
    # return HttpResponse('request')
    return redirect('homePage')

def profile_index(request):
    return render(request,'profile.html')
