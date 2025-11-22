from django.db import connection
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.subjects.models import Subjects


class SerializerSubjects (DocumentSerializer):
    class Meta:
        model = Subjects
        fields ='__all__'