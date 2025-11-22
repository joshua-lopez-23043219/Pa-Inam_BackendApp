from django.db import connection
from rest_framework.serializers import ModelSerializer

from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.registrations.models import Registration


class SerializerRegistration (DocumentSerializer):
    class Meta:
        model = Registration
        fields = '__all__'