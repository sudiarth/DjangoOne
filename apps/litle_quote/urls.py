from django.urls import path
from . import views

app_name = 'litle_quote'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>', views.quote_by_user, name='quote_by_user'),
    path('create', views.create_quote, name='create_quote'),
    path('<int:quote_id>/edit', views.edit_quote, name='edit_quote'),
    path('<int:quote_id>/delete', views.delete_quote, name='delete_quote'),
    path('search', views.search_by_user_or_email, name='search_by_user_or_email'),
    path('result/<str:query>', views.results, name='results')
]