from django.urls import path
from . import views

app_name = 'bill_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_bill, name='create_bill'),
    path('delete/<int:bill_id>', views.delete_bill, name='delete_bill'),
    path('edit/<int:bill_id>', views.edit_bill, name='edit_bill'),
]