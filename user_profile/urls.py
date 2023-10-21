from django.urls import path 
from . import views

app_name = 'profile'

urlpatterns=[
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('change_password/', views.change_password, name='change_password'),
]