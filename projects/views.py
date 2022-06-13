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
    projects = Projects.get_by_owner(owner)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'registration/profile.html', {"form":form, "projects":projects})


@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Projects.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'find.html', {"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'find.html', {"message": message})


def get_project(request, id):
    project = Projects.objects.get(pk = id)
        
    return render(request, "projects.html", {"project":project})


# add project
@login_required(login_url='/accounts/login/')
def add_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new-project.html', {"form": form})