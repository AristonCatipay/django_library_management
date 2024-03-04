from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.view_course, name='view_course'),
    path('create/', views.create_course, name='create_course'),
    path('update/<int:primary_key>/', views.update_course, name='update_course'),
    path('delete/<int:primary_key>/', views.delete, name='delete'),
]