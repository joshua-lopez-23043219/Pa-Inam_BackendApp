from rest_framework.routers import DefaultRouter


from Apps.groups.API.GroupsAPI import GroupsViewSet

routerGroups = DefaultRouter()

routerGroups.register(r'Groups', GroupsViewSet ,basename='Groups')