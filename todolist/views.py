import datetime
from operator import imod
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from todolist.models import Task
from todolist.forms import CreateTaskForm

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core import serializers

from django.http import JsonResponse

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    
    data_Task = Task.objects.filter(user=request.user)
    context = {
    'name_user' : 'Thare',
    'data' : data_Task,
    'last_login': request.COOKIES['last_login'],
    }

    return(render(request, "todolist.html",context))

def crate_task_ajax(request):
    form = CreateTaskForm()
    data = Task.objects.all()
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
        return redirect('todolist:show_todolist')

    context = {'form': form}
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Task telah berhasil dibuat!')
        return redirect('todolist:show_todolist')

    context = {'form': form}
    return render(request, 'new_task.html', context)

def signup_user(request):
    form = UserCreationForm(request.POST)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'signup.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            
            return response
            
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data =  Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def ajax_mode(request):
    data_Task = Task.objects.all()
    return JsonResponse({
        "task": list(data_Task.values())
    })