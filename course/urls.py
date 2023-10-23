from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
]