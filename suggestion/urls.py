from django.urls import path
from . import views

app_name = 'suggestion'

urlpatterns = [
    path('', views.view_suggestion, name='view_suggestion'),
    path('create/', views.create_suggestion, name='create_suggestion'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
]