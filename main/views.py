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

    return render(request,'signup.html',locals())

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
    return redirect('homePage')

def profile_index(request):
    # forms=ProfileForm
    all_profile = Profile.objects.all()
    profile = Profile.objects.get(user_id = request.user)

    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    return render(request,'profile.html', locals())

# def save_profile(request):
#     all_profile = request.Post.get('profile')
#     user_id = request.POST.get('user_id')
#
#     all_profile = Profile.objects.create(user_id=user,profile=profile)
#     return redirect('profile')
