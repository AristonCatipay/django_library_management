from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('read/', views.read_book, name='read_book'),
    path('detail/read/<int:book_primary_key>/', views.read_book_detail, name='read_book_detail'),
    path('create/', views.create_book, name='create_book'),
    path('update/<int:book_primary_key>/', views.update_book, name='update_book'),
    path('author/add/', views.add_author, name='add_author'),
    path('author-in-list/add/<int:primary_key>/', views.add_author_in_author_list, name='add_author_in_author_list'),
]