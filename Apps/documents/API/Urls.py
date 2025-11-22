from rest_framework.routers import DefaultRouter

from Apps.documents.API.DocumentsAPI import DocumentsViewSet

routerDocuments = DefaultRouter()

routerDocuments.register(r'Documents', DocumentsViewSet ,basename='Documents')