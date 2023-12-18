from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_thesis),
    path('author/read/', views.read_author),
]