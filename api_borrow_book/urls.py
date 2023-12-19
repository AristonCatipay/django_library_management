from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.read_borrow_book),
    path('borrow-request/read/', views.read_borrow_request),
    path('pickup/read/', views.read_book_pick_up),
    path('borrow-request/create/<int:book_primary_key>/', views.create_borrow_book),
    path('approve/<int:borrow_book_primary_key>/', views.approve_borrow_request),
    path('pickup/<int:borrow_book_primary_key>/', views.approve_book_pick_up),
]