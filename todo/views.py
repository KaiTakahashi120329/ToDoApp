from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoModel

class ToDoList(ListView):
    template_name = 'list.html'
    model = ToDoModel