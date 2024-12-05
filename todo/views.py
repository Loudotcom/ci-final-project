# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Task

class HomePage(TemplateView):
    """
    Displays home page"
    """

class Task(generic.ListView):
    model = Task
    template_name = 'base.html'
