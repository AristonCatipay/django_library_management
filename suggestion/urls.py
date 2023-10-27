from django.urls import path
from . import views

app_name = 'suggestion'

urlpatterns = [
    path('', views.index, name='index'),
]