from django.db import connection
from rest_framework.serializers import ModelSerializer

from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.teachers.models import Teachers


class SerializerTeachers (DocumentSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'