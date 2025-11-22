from django.db import connection
from rest_framework.serializers import ModelSerializer

from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.notes.models import Notes


class SerializerNotes (DocumentSerializer):
    class Meta:
        model = Notes
        fields ='__all__'