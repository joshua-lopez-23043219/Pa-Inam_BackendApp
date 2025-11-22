from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



from Apps.teachers.API.SerializerTeachers import SerializerTeachers
from Apps.teachers.models import Teachers


class TeachersViewSet (ModelViewSet):

    queryset = Teachers.objects.all()
    serializer_class = SerializerTeachers
 # ========== LISTADO COMPLETO ==========
    @action(methods=['get'], detail=False, url_path='listar-maestros')
    def listar_maestros(self, request):
        maestros = self.get_queryset()
        serializer = self.get_serializer(maestros, many=True)
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

        maestro = Teachers.objects(code_teacher=codigo).first()
        if not maestro:
            return Response(
                {"error": "Maestro no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(maestro)
        return Response(serializer.data)