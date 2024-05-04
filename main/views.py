from rest_framework import generics, status
from rest_framework.response import Response

from main.models import Company, Contact
from main.serializers import CompanySerializer, ContactSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = Company.objects.filter(id=self.kwargs['pk']).first()
        if company is not None:
            contact = Contact.objects.create(
                email=serializer.data['email'],
                country=serializer.data['country'],
                city=serializer.data['city'],
                street=serializer.data['street'],
                house_number=serializer.data['house_number'],
                company=company
            )
            contact.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Объет компании не найден'}, status=status.HTTP_400_BAD_REQUEST)
