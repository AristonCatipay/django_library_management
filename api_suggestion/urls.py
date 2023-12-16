from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_suggestion),
    path('create/', views.create_suggestion),
    path('update/<int:pk>/', views.update_suggestion),
    path('delete/<int:pk>/', views.delete_suggestion),
]
