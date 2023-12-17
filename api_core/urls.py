from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('statistics/', views.read_statistics),
    path('users/', views.read_user),
    path('logout/', views.logout),
]