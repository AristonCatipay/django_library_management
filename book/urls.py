from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('detail/<int:primary_key>/', views.detail, name='detail'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
]