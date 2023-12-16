from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_suggestion),
    path('create/', views.create_suggestion),
]
