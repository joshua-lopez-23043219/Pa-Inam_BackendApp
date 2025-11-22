from rest_framework.routers import DefaultRouter


from Apps.subjects.API.SubjectsAPI import SubjectsViewSet

routerSubjects = DefaultRouter()

routerSubjects.register(r'Subjects', SubjectsViewSet ,basename='Subjects')