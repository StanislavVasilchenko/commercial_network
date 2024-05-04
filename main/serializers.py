from rest_framework import serializers

from main.models import Company, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()

    def get_contacts(self, obj):
        contacts = Contact.objects.filter(company=obj)
        return ContactSerializer(contacts, many=True).data

    class Meta:
        model = Company
        fields = ['status', 'name', 'provider', 'debt', 'contacts']
