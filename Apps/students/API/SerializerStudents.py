from django.db import connection
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.students.models import Student


class SerializerStudents (DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'


