from django.urls import path
from . import views

app_name = 'thesis'

urlpatterns = [
    path('', views.view_thesis, name='view_thesis'),
    path('add/', views.add, name='add'),
    path('detail/<int:primary_key>/', views.detail, name='detail'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
    path('author/add/', views.add_author, name='add_author'),
    path('author-in-list/add/<int:primary_key>/', views.add_author_in_author_list, name='add_author_in_author_list'),
    path('view_file/<str:file_location>/', views.view_file, name='view_file'),
]