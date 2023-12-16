from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_course),
    path('create/', views.create_course),
]