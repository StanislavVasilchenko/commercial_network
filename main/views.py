from rest_framework import generics

from main.models import Company
from main.serializers import CompanySerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
