from django.urls import path
from . import views

urlpatterns = [
  path('todos/create/', views.create, name='todo-create'),
]
