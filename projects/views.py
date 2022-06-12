from django.shortcuts import render,redirect

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    projects = Projects.get_projects()

    return render(request,'home.html',{"projects":projects})



@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    owner = current_user
    projects = Projects.get_by_author(owner)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'registration/profile.html', {"form":form, "projects":projects})