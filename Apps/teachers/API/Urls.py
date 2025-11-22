from rest_framework.routers import DefaultRouter


from Apps.teachers.API.TeachersAPI import TeachersViewSet

routerTeachers = DefaultRouter()

routerTeachers.register(r'Teachers', TeachersViewSet ,basename='Teachers')