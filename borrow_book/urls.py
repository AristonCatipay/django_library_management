from django.urls import path
from . import views

app_name = 'borrow_book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:primary_key>', views.add, name='add'),
    path('borrow-request/', views.borrow_request, name='borrow_request'),
]