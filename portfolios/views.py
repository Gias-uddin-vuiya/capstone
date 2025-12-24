from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Porject

# Create your views here.

def index(request):
    profile = Profile.objects.all()  # resive all profile objects
    
    return render(request, "makers_portfolio/index.html", {
        "profile": profile[0] if profile else None
    })


def project(request):
    project_page = Porject.objects.all()
    return render(request, "makers_portfolio/project.html", {  
        "project_page": project_page
    })

def projects(request):
    return render(request, "makers_portfolio/projects.html", {  
        
    })

# english project
def english(request):
    return render(request, "makers_portfolio/english-project.html", {  
        
    })

def art(request):
    return render(request, "makers_portfolio/art-project.html", {  
        
    })