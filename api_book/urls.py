from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_book),
    path('read/detail/<int:book_primary_key>/', views.read_book_detail),
    path('create/', views.create_book),
    path('update/<int:book_primary_key>/', views.update_book),
    path('delete/<int:book_primary_key>/', views.delete_book),
    path('author/read/', views.read_author),
    path('author/create/', views.create_author),
]