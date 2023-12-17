from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:book_id>/', views.create_review),
]