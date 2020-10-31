from django.urls import path
from .views import ToDoList, ToDoDetail, ToDoCreate


urlpatterns = [
    path('list/', ToDoList.as_view(), name='list'),
    path('detail/<int:pk>/', ToDoDetail.as_view(), name='detail'),
    path('create/', ToDoCreate.as_view(), name='create'),
]
