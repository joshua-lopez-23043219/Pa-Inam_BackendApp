from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.imparte.API.SerializerImparte import SerializerImparte
from Apps.imparte.models import Imparte


class ImparteViewSet (ModelViewSet):

    queryset = Imparte.objects.all()
    serializer_class = SerializerImparte
