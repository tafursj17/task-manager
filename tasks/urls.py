from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/create_note/', views.create_note, name='create_note'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/notes/<int:note_id>', views.note_detail, name='note_detail'),
    path('tasks/<int:task_id>/notes/<int:note_id>/delete', views.delete_note, name='delete_note')
]
