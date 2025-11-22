from django.db import connection
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.tutors.models import Tutor


class SerializerTutors (DocumentSerializer):
    class Meta:
        model = Tutor
        fields ='__all__'