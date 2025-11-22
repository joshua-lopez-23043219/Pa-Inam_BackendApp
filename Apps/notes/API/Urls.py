from rest_framework.routers import DefaultRouter

from Apps.notes.API.NotesAPI import NotesViewSet

routerNotes = DefaultRouter()

routerNotes.register(r'Note',  NotesViewSet,basename='Note')