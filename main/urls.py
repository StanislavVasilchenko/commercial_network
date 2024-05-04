from django.urls import path

from main.apps import MainConfig
from main.views import CompanyCreateAPIView, CompanyListAPIView, ContactCreateAPIView

app_name = MainConfig.name

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create-company'),
    path('list/', CompanyListAPIView.as_view(), name='list-company'),


    path('contact/create/<int:pk>/', ContactCreateAPIView.as_view(), name='create-contacts'),
]