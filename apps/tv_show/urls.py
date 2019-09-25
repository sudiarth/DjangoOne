from django.urls import path
from . import views

app_name = 'tv_show'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('results/<str:query>', views.results, name='results'),
    path('movie/<int:movie_id>/like', views.create_like, name='create_like'),
    path('movie/<int:movie_id>/unlike', views.delete_like, name='delete_like')
]