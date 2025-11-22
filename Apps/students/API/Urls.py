from rest_framework.routers import DefaultRouter

from Apps.students.API.StudentsAPI import StudentsViewSet

routerStudents = DefaultRouter()

routerStudents.register(r'students', StudentsViewSet ,basename='students')