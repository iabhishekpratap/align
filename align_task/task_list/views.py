from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.tasks import task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .models import Task

# View to list all tasks
def list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list/list.html', {'tasks': tasks})

# View to create a new task
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list:list')
    return render(request, 'task_list/create.html') 

# view to update an existing task
def update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list:list')
    return render(request, 'task_list/update.html', {'task': task})

# delete view to delete a task
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list:list')

    return render(request, 'task_list/delete.html', {'task': task})

# login page view
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "invalid credentials.")
            return redirect('task_list:login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.error(request, "invalid credentials.")
            return redirect('task_list:login')
        
        
        login(request, user)
        return redirect('task_list:list')

# register page view
def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('task_list:register')

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('task_list:login')

    return render(request, 'task_list/register.html')