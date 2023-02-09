from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

@login_required
def tasks(request):
    # task = get_object_or_404(Task, id = id)
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

@login_required
def tasks_completed(request):
    # task = get_object_or_404(Task, id = id)
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

@login_required
def create_task(request):   
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask
    })
    else:
        form = CreateNewTask(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        messages.success(request, 'Tarea Creada con exitó')
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(pk=task_id, user=request.user)
        form = CreateNewTask(instance=task)
        return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form
        })
    else:
        task = Task.objects.get(pk=task_id,  user=request.user)
        form = CreateNewTask(request.POST, instance=task)
        messages.success(request, 'Tarea Actualizada con exitó')
        form.save()
        return redirect('tasks')

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        messages.success(request, 'Tarea Completada con exitó')
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarea Eliminada con exitó')
        return redirect('tasks')









   
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })