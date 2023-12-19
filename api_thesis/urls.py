from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_thesis),
    path('create/', views.create_thesis),
    path('update/<int:thesis_primary_key>/', views.update_thesis),
    path('author/read/', views.read_author),
    path('author/create/', views.create_author),
    path('author/update/<int:author_primary_key>/', views.update_author),
    path('authorlist/read/', views.read_author_list),
    path('authorlist/create/', views.create_author_list),
    path('authorlist/update/<int:author_list_primary_key>/', views.update_author_list)
]