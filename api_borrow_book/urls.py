from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_borrow_book),
    path('borrow-request/read/', views.read_borrow_request),
    path('create/<int:book_primary_key>/', views.create_borrow_book),
]