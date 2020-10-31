from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import ToDoModel
from django.urls import reverse_lazy

class ToDoList(ListView):
    template_name = 'list.html'
    model = ToDoModel

class ToDoDetail(DetailView):
    template_name = 'datail.html'
    model = ToDoModel

class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = ToDoModel
    fields = ['title', 'memo', 'priority', 'duedate']
    success_url = reverse_lazy('list')

class ToDoDelete(DeleteView):
    template_name = 'delete.html'
    model = ToDoModel
    success_url = reverse_lazy('list')
    