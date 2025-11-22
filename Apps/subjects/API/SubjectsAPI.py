from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.subjects.API.SerializerSubjects import SerializerSubjects
from Apps.subjects.models import Subjects


class SubjectsViewSet (ModelViewSet):

    queryset = Subjects.objects.all()
    serializer_class = SerializerSubjects
