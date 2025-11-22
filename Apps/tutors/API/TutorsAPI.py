from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



from Apps.tutors.API.SerializerTutors import SerializerTutors
from Apps.tutors.models import Tutor

class TutorsViewSet (ModelViewSet):

    queryset = Tutor.objects.all()
    serializer_class = SerializerTutors
