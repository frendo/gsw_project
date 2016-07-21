from django.shortcuts import render
from django.conf import settings

def angular(request):
    return render(request, 'angular/angular.html', {})
