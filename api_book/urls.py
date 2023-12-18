from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_book),
    path('read/detail/<int:book_primary_key>/', views.read_book_detail),
]