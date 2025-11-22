from rest_framework.routers import DefaultRouter


from Apps.registrations.API.RegistrationAPI import RegistrationViewSet

routerRegistrations = DefaultRouter()

routerRegistrations.register(r'Registration', RegistrationViewSet ,basename='Registration')