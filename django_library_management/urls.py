"""
URL configuration for django_library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Imports for showing images.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user-profile/', include('user_profile.urls')),
    path('address/', include('address.urls')),
    path('course/', include('course.urls')),
    path('thesis/', include('thesis.urls')),
    path('book/', include('book.urls')),
    path('suggestion/', include('suggestion.urls')),
    path('borrow-book/', include('borrow_book.urls')),
    path('review/', include('review.urls')),
    path('api/suggestion/', include('api_suggestion.urls')),
    path('api/course/', include('api_course.urls')),
    path('api/review/', include('api_review.urls')),
    path('api/core/', include('api_core.urls')),
    path('api/book/', include('api_book.urls')),
    path('api/thesis/', include('api_thesis.urls')),
    path('api/borrow-book/', include('api_borrow_book.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
