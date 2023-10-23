from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
    path('delete/<int:primary_key>/', views.delete, name='delete'),
]