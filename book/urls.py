from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.view_book, name='view_book'),
    path('detail/<int:book_primary_key>/', views.view_book_detail, name='view_book_detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
    path('author/add/', views.add_author, name='add_author'),
    path('author-in-list/add/<int:primary_key>/', views.add_author_in_author_list, name='add_author_in_author_list'),
]