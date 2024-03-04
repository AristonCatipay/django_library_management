from django.urls import path
from . import views

app_name = 'suggestion'

urlpatterns = [
    path('', views.view_suggestion, name='view_suggestion'),
    path('add/', views.add, name='add'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
]