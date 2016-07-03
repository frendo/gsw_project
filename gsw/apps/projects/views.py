from django.shortcuts import render
from .models import Project
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def project_list(request):
    projects = Project.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    return render(request, 'projects/project_list.html', {'projects' : projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
