from django.urls import path
from . import views

app_name = 'project_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_project, name='create_project'),
    path('edit/<int:project_id>', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>', views.delete_project, name='delete_project'),
    path('create/task/<int:project_id>', views.create_task, name='create_task'),
    path('project/<int:project_id>', views.view_task, name='view_task'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),
]