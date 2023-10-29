from django.urls import path
from . import views

app_name = 'borrow_book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:primary_key>', views.add, name='add'),
    path('borrow-request/', views.borrow_request, name='borrow_request'),
    path('borrow-request-approve/<int:primary_key>/', views.borrow_request_approve, name='borrow_request_approve'),
    path('book-pick-up/', views.book_pick_up, name='book_pick_up'),
]