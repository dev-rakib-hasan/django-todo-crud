from django.urls import path
from . import views

urlpatterns = [
  path('todos/create/', views.create, name='todo-create'),
  path('todos/<int:pk>/update', views.update, name = 'todo-update'),
]
