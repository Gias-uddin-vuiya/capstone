
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import get_object_or_404, render
from .models import Profile, Porject, Projects, ProjectImage 

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

    
def project_detail(request, slug):
    project = get_object_or_404(Projects, slug=slug, isActive=True)

    # Ordered queryset
    projects = list(
        Projects.objects.filter(isActive=True).order_by("created_at")
    )

    current_index = projects.index(project)

    previous_project = projects[current_index - 1] if current_index > 0 else None
    next_project = (
        projects[current_index + 1]
        if current_index < len(projects) - 1
        else None
    )

    return render(request, "makers_portfolio/project_detail.html", {
        "project": project,
        "details": project.details,
        "previous_project": previous_project,
        "next_project": next_project,
    })

def project_image_detail(request, slug):
    image = ProjectImage.objects.select_related("project").get(slug=slug)

    return render(request, "makers_portfolio/projects/image_detail.html", {
        "image": image
    })

def project_pdf(request, slug):
    project = get_object_or_404(Projects, slug=slug, isActive=True)
    details = project.details

    html_string = render_to_string(
        "makers_portfolio/pdf/project_pdf.html",
        {"details": details}
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{project.slug}.pdf"'
    return response