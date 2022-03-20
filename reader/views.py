import os.path

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import PDF


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def pdf1(request):
    pdf = PDF.objects.all()

    data = {
        'pdf': pdf
    }
    return render(request, 'pdf1.html', data)
