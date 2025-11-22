from rest_framework.routers import DefaultRouter


from Apps.imparte.API.ImparteAPI import ImparteViewSet

routerImparte = DefaultRouter()

routerImparte.register(r'Imparte', ImparteViewSet ,basename='Imparte')