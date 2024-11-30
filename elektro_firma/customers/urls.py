from django.urls import path
from .views import CustomerUpdateView


urlpatterns = [
    path('customer/<int:pk>/edit/', CustomerUpdateView.as_view(), name='edit_customer'),
]