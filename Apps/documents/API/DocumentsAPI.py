from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.documents.API.SerializerDocuments import SerializerDocuments
from Apps.documents.models import Documents


class DocumentsViewSet (ModelViewSet):

    queryset = Documents.objects.all()
    serializer_class = SerializerDocuments
