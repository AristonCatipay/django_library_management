from django.urls import path
from . import views

app_name = 'borrow_book'

urlpatterns = [
    path('', views.index, name='index'),
]