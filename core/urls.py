from django.urls import path
from . import views

appname = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]