from django.db import connection
from rest_framework.serializers import ModelSerializer

from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.imparte.models import Imparte


class SerializerImparte (DocumentSerializer):
    class Meta:
        model = Imparte
        fields = '__all__'