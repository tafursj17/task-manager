from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
]
