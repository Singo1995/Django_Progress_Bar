from django.contrib import admin
from django.urls import path, include
from accounts.api.views import UserRegistrationAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    ]