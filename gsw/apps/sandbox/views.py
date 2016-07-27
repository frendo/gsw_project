from django.shortcuts import render
from .models import App
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def 
def app_list(request):
    apps = App.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    return render(request, 'apps/apps.html', {'apps' : apps})

def app_detail(request, pk):
    app = get_object_or_404(Sandbox, pk=pk)
    return render(request, 'apps/app_detail.html', {'app': app})
