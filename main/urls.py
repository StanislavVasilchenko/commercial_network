from django.urls import path

from main.apps import MainConfig
from main.views import (CompanyCreateAPIView, CompanyListAPIView, ContactCreateAPIView,
                        CompanyDetailAPIView, CompanyUpdateAPIView, CompanyDeleteAPIView)

app_name = MainConfig.name

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create-company'),
    path('list/', CompanyListAPIView.as_view(), name='list-company'),
    path('company/<int:pk>/', CompanyDetailAPIView.as_view(), name='profile-company'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='update-company'),
    path('delete/<int:pk>/', CompanyDeleteAPIView.as_view(), name='delete-company'),

    #  Contacts urls
    path('contact/create/<int:pk>/', ContactCreateAPIView.as_view(), name='create-contacts'),
]