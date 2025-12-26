from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile, Porject, Projects  

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
    projects = Projects.objects.filter(isActive=True)
    return render(request, "makers_portfolio/projects.html", {  
        "projects": projects
    })

# will work here later
# def project_detail(request, slug):
#     project = get_object_or_404(Projects, slug=slug, isActive=True)
#     return render(request, "makers_portfolio/project_detail.html", {
#         "project": project
#     })


# english project
def english(request):
    return render(request, "makers_portfolio/english-project.html", {  
        
    })

def art(request):
    return render(request, "makers_portfolio/art-project.html", {  
        
    })