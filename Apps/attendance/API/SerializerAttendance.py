from django.db import connection
from rest_framework.serializers import ModelSerializer

from rest_framework_mongoengine.serializers import DocumentSerializer


from Apps.attendance.models import Attendance


class SerializerAttendance (DocumentSerializer):
    class Meta:
        model = Attendance
        fields ='__all__'

