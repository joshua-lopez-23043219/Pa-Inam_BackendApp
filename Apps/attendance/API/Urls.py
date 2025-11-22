from rest_framework.routers import DefaultRouter

from Apps.attendance.API.AttendanceAPI import AttendanceViewSet

routerAttendance = DefaultRouter()

routerAttendance.register(r'Attendance', AttendanceViewSet ,basename='Attendance')