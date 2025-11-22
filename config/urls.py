"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)


from Apps.attendance.API.Urls import routerAttendance
from Apps.documents.API.Urls import routerDocuments
from Apps.groups.API.Urls import routerGroups
from Apps.imparte.API.Urls import routerImparte
from Apps.notes.API.Urls import routerNotes
from Apps.registrations.API.Urls import routerRegistrations
from Apps.students.API.Urls import routerStudents
from Apps.subjects.API.Urls import routerSubjects
from Apps.teachers.API.Urls import routerTeachers
from Apps.tutors.API.Urls import routerTutors

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),  # sin autenticación para ver Swagger

)




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/',include(routerStudents.urls)),
    path('attendance/',include(routerAttendance.urls)),
    path('documents/',include(routerDocuments.urls)),
    path('groups/',include(routerGroups.urls)),
    path('imparte/',include(routerImparte.urls)),
    path('notes/',include(routerNotes.urls)),
    path('registrtions/',include(routerRegistrations.urls)),
    path('subjects/',include(routerSubjects.urls)),
    path('teachers/',include(routerTeachers.urls)),
    path('tutor/',include(routerTutors.urls)),

## Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
