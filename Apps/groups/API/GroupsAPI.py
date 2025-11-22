from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.groups.API.SerializerGroups import SerializerGroups
from Apps.groups.models import Groups


class GroupsViewSet (ModelViewSet):

    queryset =Groups.objects.all()
    serializer_class = SerializerGroups
# ========== LISTADO COMPLETO ==========
    @action(methods=['get'], detail=False, url_path='listar-grupos')
    def listar_grupos(self, request):
        grupos = self.get_queryset()
        serializer = self.get_serializer(grupos, many=True)
        return Response(serializer.data)

    # ========== BUSCAR POR CÓDIGO ==========
    @action(methods=['get'], detail=False, url_path='buscar-por-codigo')
    def buscar_por_codigo(self, request):
        codigo = request.query_params.get('codigo')
        if not codigo:
            return Response(
                {"error": "Debes enviar el parámetro ?codigo="},
                status=status.HTTP_400_BAD_REQUEST
            )

        grupo = Group.objects(code_group=codigo).first()
        if not grupo:
            return Response(
                {"error": "Grupo no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(grupo)
        return Response(serializer.data)
