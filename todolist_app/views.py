from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        return redirect('todolist')
    else: 
        #all_task = Task.objects.all()
        all_task = Task.objects.filter(manage=request.user)
        paginator = Paginator(all_task,5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html',{'all_task':all_task})
@login_required        
def delete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')
@login_required
def edit_task(request,task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
@login_required
def complete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')
@login_required
def pending_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')
def contact(request):
    context = {
        'contact_text': "Welcome to contact page."
    }
    return render(request, 'contact.html',context)
def index(request):
    context = {
        'index_text': "Welcome to home page."
    }
    return render(request, 'index.html',context)
def about(request):
    context = {
        'about_text': "Welcome to about page."
    }
    return render(request, 'about.html',context)