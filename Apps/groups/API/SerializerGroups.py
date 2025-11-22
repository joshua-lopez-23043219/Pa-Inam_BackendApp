from django.db import connection
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer

from Apps.groups.models import Groups


class SerializerGroups (DocumentSerializer):
    class Meta:
        model = Groups
        fields ='__all__'
