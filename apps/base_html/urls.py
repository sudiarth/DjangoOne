from django.urls import path
from . import views

app_name = 'base_html'

urlpatterns = [
    path('', views.index, name='index')
]