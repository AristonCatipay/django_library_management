from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_course),
    path('create/', views.create_course),
    path('update/<int:pk>/', views.update_course),
]