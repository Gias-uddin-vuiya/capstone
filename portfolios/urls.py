from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('projects/english/', views.english, name='english'),
]