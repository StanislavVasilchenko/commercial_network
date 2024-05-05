from rest_framework import generics, status
from rest_framework.response import Response

from main.models import Company, Contact
from main.permissions import UserPermissions
from main.serializers import CompanySerializer, ContactSerializer, CompanyUpdateSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (UserPermissions,)


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (UserPermissions,)


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (UserPermissions,)


class CompanyUpdateAPIView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = (UserPermissions,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'debt' in request.data:
            return Response({'error': f'Вы не можете обновлять поле задолженность для {instance.name}'},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)


class CompanyDeleteAPIView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (UserPermissions,)


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (UserPermissions,)

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
