from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "makers_portfolio/index.html", {
        
    })


def project(request):
    return render(request, "makers_portfolio/project.html", {  
        
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