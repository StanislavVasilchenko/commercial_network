from django.urls import path

from main.apps import MainConfig
from main.views import CompanyCreateAPIView

app_name = MainConfig.name

urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='create-company')
]