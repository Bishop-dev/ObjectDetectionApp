from django.shortcuts import render
from django.views import generic

from .models import Person


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, 'face_detection/index.html', context)


# def add_person(request):
#


# class IndexView(generic.ListView):
#     template_name = 'face_detection/index.html'
