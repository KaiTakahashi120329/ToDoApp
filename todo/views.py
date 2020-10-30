from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoModel

class ToDoList(ListView):
    template_name = 'list.html'
    model = ToDoModel

class ToDoDetail(DetailView):
    template_name = 'datail.html'
    model = ToDoModel