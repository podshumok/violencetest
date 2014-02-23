from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from .models import ViolentPhoto, Theme


def result(request, theme):
    theme = get_object_or_404(Theme, short_name=theme)

    vp = ViolentPhoto.objects.filter(theme=theme).all()

    data = {}

    for obj in vp:
        if obj.violent_level in data:
             data[obj.violent_level].append(obj)
        else:
             data[obj.violent_level] = list()

    return render_to_response('result.html', {'photos': data})


def index(request, theme):
    return HttpResponse('')
