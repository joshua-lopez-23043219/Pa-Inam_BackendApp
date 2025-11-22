from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.attendance.API.SerializerAttendance import SerializerAttendance
from Apps.attendance.models import Attendance


class AttendanceViewSet (ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = SerializerAttendance
