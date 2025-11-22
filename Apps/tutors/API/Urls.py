from rest_framework.routers import DefaultRouter


from Apps.tutors.API.TutorsAPI import TutorsViewSet

routerTutors = DefaultRouter()

routerTutors.register(r'Tutors', TutorsViewSet ,basename='Tutors')