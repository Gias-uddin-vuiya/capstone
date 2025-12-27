from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),

    path('projects/', views.projects, name='projects'),
    path('projects/image/<slug:slug>/', views.project_image_detail, name='project_image_detail'),   
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    
]