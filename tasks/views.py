from django.http import HttpResponse
from .models import Task, Note
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewNote
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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
    return render(request, 'tasks/tasks_completed.html',{
        'tasks': tasks
    })

@login_required
def create_task(request):   
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask ,
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
        notes = Note.objects.filter(task = task_id)
        return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form,
            'notes': notes
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


@login_required
def create_note(request, task_id):
    if request.method == 'GET':
        form = CreateNewNote(request.POST)
        return render(request, 'tasks/create_note.html',{
        'form': form,
        })
    else:
        form = CreateNewNote(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.task = Task.objects.get(pk=task_id)
            messages.success(request, 'Nota Creada con exitó')
            new_comment.save()
        return redirect(f'/tasks/{task_id}/')
    

@login_required
def note_detail(request, task_id, note_id):
    if request.method == 'GET':
        task = Task.objects.get(pk=task_id)
        note = Note.objects.get(pk=note_id)
        form = CreateNewNote(instance=note)
        return render(request, 'tasks/note_detail.html',{
            'note': note,
            'form': form,
            'task': task
        })
    else:
        task = Task.objects.get(pk=task_id)
        note = Note.objects.get(pk=note_id)
        form = CreateNewNote(request.POST, instance=note)
        messages.success(request, 'Nota Actualizada con exitó')
        form.save()
        return redirect(f'/tasks/{task_id}/')

@login_required
def delete_note(request, task_id, note_id):
    task = Task.objects.get(pk=task_id)
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Nota Eliminada con exitó')
        return redirect(f'/tasks/{task_id}/')

    