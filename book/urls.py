from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('read/', views.read_book, name='read_book'),
    path('detail/read/<int:book_primary_key>/', views.read_book_detail, name='read_book_detail'),
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:primary_key>/', views.edit, name='edit'),
    path('author/add/', views.add_author, name='add_author'),
    path('author-in-list/add/<int:primary_key>/', views.add_author_in_author_list, name='add_author_in_author_list'),
]