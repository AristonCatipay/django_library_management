from django.urls import path 
from . import views

app_name = 'profile'

urlpatterns=[
    path('', views.index, name='index'),
    path('update/', views.update_profile, name='update_profile'),
    path('address/update/', views.update_address, name='update_address'),
    path('address/update/province/load/', views.load_province, name='load_province'),
    path('address/update/city/municipality/load/', views.load_city_municipality, name='load_city_municipality'),
    path('address/update/barangay/load/', views.load_barangay, name='load_barangay'),
    path('password/update/', views.update_password, name='update_password'),
]