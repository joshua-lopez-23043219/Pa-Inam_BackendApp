from django.db import connection
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.documents.models import Documents


class SerializerDocuments (DocumentSerializer):
    class Meta:
        model = Documents
        fields = '__all__'