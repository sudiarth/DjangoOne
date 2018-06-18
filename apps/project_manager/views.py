from django.shortcuts import render, redirect
from . import models as m
from django.contrib import messages
from apps.auth_user.models import User

def index(request):

    if 'user_id' in request.session:
        
        projects = m.Project.objects.filter(user_id=request.session['user_id']).order_by('-created_at')
        context = {
            'projects' : projects
        }
        return render(request, 'project_manager/index.html', context)

    return redirect('auth_user:index')

def create_project(request):
    if 'user_id' in request.session:
        
        user = User.objects.get(id=request.session['user_id'])

        if request.method == 'POST':
            project = m.Project()
            project.title = request.POST['title']
            project.user = user
            project.save()
        
        return redirect('project_manager:index')

    return redirect('auth_user:index')

def edit_project(request, project_id):

    if 'user_id' in request.session:
        project = m.Project.objects.get(id=project_id)

        context = {
            'project': project
        }

        if request.method == 'POST':

            try:
                project.title = request.POST['title']
                project.save()
                return redirect('project_manager:index')

            except:
                messages.error(request, 'Project updated error')
                return render(request, 'project.manager/edit_project.html', context)

        else:
            return render(request, 'project_manager/edit_project.html', context)

    return redirect('auth_user:index')

def delete_project(request, project_id):

    if 'user_id' in request.session:

        project = m.Project.objects.get(id=project_id)
        project.delete()
        return redirect('project_manager:index')

    return redirect('auth_user:index')

def create_task(request, project_id):

    if 'user_id' in request.session:

        try:

            user = User.objects.get(id=request.session['user_id'])
            project = m.Project.objects.get(id=project_id)

            task = m.Task()
            task.description = request.POST['description']
            task.user = user
            task.project = project
            task.save()
            
        except:

            messages.error(request, 'Save task error')

        return redirect('project_manager:view_task', project_id=project.id)
    
    return redirect('auth_user:index')

def view_task(request, project_id):

    try:
    
        project = m.Project.objects.get(id=project_id)
        tasks = m.Task.objects.filter(project_id=project_id).all().order_by('-created_at')

        print(project, tasks)

        context = {
            'project' : project,
            'tasks' : tasks
        }
    except:
        context = {
            'project' : [],
            'tasks' : []
        }

    return render(request, 'project_manager/task.html', context)

def edit_task(request, task_id):

    if 'user_id' in request.session:

        task = m.Task.objects.get(id=task_id)
        project_id = task.project_id

        context = {
            'task' : task
        }

        if request.method == 'POST':
        
            try:

                task.description = request.POST['description']
                task.save()

                return redirect('project_manager:view_task', project_id=task.project_id)

            except:

                messages.error(request, 'Task save error')
                return render(request, 'project_manager/edit_task.html', context)

        else:
            return render(request, 'project_manager/edit_task.html', context)

    return redirect('auth_user:index')

def delete_task(request, task_id):
    if 'user_id' in request.session:

        task = m.Task.objects.get(id=task_id)
        task.delete()
        return redirect('project_manager:view_task', project_id=task.project_id)

    return redirect('auth_user:index')