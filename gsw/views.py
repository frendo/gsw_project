# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import now
import datetime
from gsw.apps.projects.models import Project
from django.views.decorators.cache import never_cache
from django.template.loader import get_template
from django.http import HttpResponse

@never_cache
def sw_js(request, js):
    template = get_template('gsw/service-worker.js')
    html = template.render()
    return HttpResponse(html, content_type="application/x-javascript")

def home(request):
    projects = Project.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    today = datetime.date.today() 
    return render(request, "gsw/index.html",
                  {'projects' : projects, 'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


