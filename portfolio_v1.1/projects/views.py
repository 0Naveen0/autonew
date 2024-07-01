from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects_home(request):
    projects = Project.objects.all()
    context = {
    'projects':projects
    }
    return render(request,'projects/project_home.html',context)
    
def projects_detail(request,pk): 
  
    projects = Project.objects.get(pk=pk)
    context = {
    'project':projects
    }  
    return render (request,'projects/project_detail.html',context) 