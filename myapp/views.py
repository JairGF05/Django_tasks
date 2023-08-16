from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course'
    return render(request, 'index.html', {
        'title': title,
    })

def hello(request, username):
    #concatenando el username recibido
    return HttpResponse("<h1>Hola %s</h1>" %username)

def about(request):
    username = 'jairGF'
    return render(request, 'about.html', {
        'username':username
    })

def projects(request):
    #Se convierte a lista der Python
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {
        'projects': projects
    })

def tasks(request): 
    #tasks = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, "tasks.html", {
        'tasks':tasks
    })

def create_task(request):
    #print(request.GET['title'])
    #print(request.GET['description'])
    #necesitamos saber a que proyecto pertenece 
    #Nota no debemos usar el metodo GET para insertar datos, sino POST
    if request.method =='GET':
        #show interface
         return render(request, 'create_task.html', {
        'form':CreateNewTask()
    })

    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')
   
def create_project(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'create_project.html', {
        'form':CreateNewProject()
        })
    
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    #print(id)
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'project_detail.html', {
        'project':project, 
        'tasks': tasks,
    })