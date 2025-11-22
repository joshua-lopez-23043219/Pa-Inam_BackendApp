from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.students.API.SerializerStudents import SerializerStudents
from Apps.students.models import Student


class StudentsViewSet (ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = SerializerStudents


    # @action(methods=['post'], detail=False)
    # # para insertar los datos a la vase de datos
    # def PostNote(self, request):
    #     id_registration = request.data['id_registration']
    #     id_subject = request.data.get('id_subject')
    #     first_partial = request.data.get('first_partial')
    #     second_partial = request.data.get('second_partial')
    #     first_semester = request.data.get('first_semester')
    #     third_partial = request.data.get('third_partial')
    #     quarter_partial = request.data.get('quarter_partial')
    #     second_semester = request.data.get('second_semester')
    #     final_grade = request.data.get('final_grade')
    #     special_note = request.data.get('special_note')
    #     # Guardar los datos en la base de datos
    #     NoteSave = Note(id_registration=id_registration,id_subject=id_subject, first_partial=first_partial, second_partial=second_partial,
    #                         first_semester=first_semester, third_partial=third_partial, quarter_partial=quarter_partial,
    #                         second_semester=second_semester,  final_grade=final_grade, special_note=special_note)
    #     NoteSave.save()
    #     Mensaje = { f'{id_registration} -{id_subject} - {first_partial} - {second_partial} -'
    #                        f'{first_semester} - {third_partial} - {quarter_partial} -'
    #                        f'{second_semester} - {final_grade} - {special_note}'}
    #
    #     data = ResponseData(
    #         Success=True,
    #         Status=status.HTTP_200_OK,
    #         Message='Nota registrada',
    #         Record=Mensaje
    #     )



        # return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['get'], detail=False)
    def ListStudents(self, request):
        try:
            estudiantes = Student.objects.all()
            serializer = SerializerStudents(estudiantes, many=True)



            return Response({
                "Success": True,
                "Status": status.HTTP_200_OK,
                "Message": "Listado de estudiantes",
                "Record": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "Success": False,
                "Status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "Message": f"Error al listar estudiwantes: {str(e)}",
                "Record": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # ========== BUSCAR POR CÓDIGO ==========

    @action(methods=['get'], detail=False, url_path='buscar-por-codigo')
    def buscar_por_codigo(self, request):
        codigo = request.query_params.get('codigo')
        if not codigo:
            return Response(
                {"error": "Debes enviar el parámetro ?codigo="},
                status=status.HTTP_400_BAD_REQUEST
            )

        estudiante = Student.objects(code_student=codigo).first()
        if not estudiante:
            return Response(
                {"error": "Estudiante no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(estudiante)
        return Response(serializer.data)



    #crea una lista de las notas de los estudiantes
    # @action(methods=['get'], detail=False)
    # def DetalleNota(self, request):
    #     SP_Detalle_Nota = 'SP_Detalle_Nota'
    #     resultados = Procedimeinto_SP_Detalle_Nota(SP_Detalle_Nota)
    #
    #     data = ResponseData(
    #         Success=True,
    #         Status=status.HTTP_200_OK,
    #         Message='Detalle de las notas',
    #         Record=resultados
    #     )
    #     return Response(data=data.toResponse(), status=status.HTTP_200_OK)
    #
    # @action(methods=['get'], detail=False)
    # def Specific_Detalle_Docuento(self, request):
    #     code_student = request.query_params.get('code_student')
    #     if not code_student:
    #         return Response(
    #             data={"message": "code_student es requerido"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #     nombre_procedimiento = 'SP_Specific_Detalle_Nota'
    #     parametros = [code_student]
    #     resultados = Procedimeinto_SP_Specific_Detalle_Nota(nombre_procedimiento, parametros)
    #
    #     data = ResponseData(
    #         Success=True,
    #         Status=status.HTTP_200_OK,
    #         Message='Información nota Estudiante',
    #         Record=resultados
    #     )
    #     return Response(data=data.toResponse(), status=status.HTTP_200_OK)
    #
    #
    #
    # @action(methods=['post'], detail=False)
    # def UpdateNote(self, request):
    #     NoteBD = Note.objects.get(id=request.data.get('id'))
    #     NoteSerializer = SerializerNote(NoteBD, request.data)
    #     if NoteSerializer.is_valid():
    #         NoteSerializer.save()
    #
    #         data = ResponseData(
    #             Success=True,
    #             Status=status.HTTP_200_OK,
    #             Message='Nota Actualizada',
    #             Record=NoteSerializer
    #         )
    #         return Response( data= data.toResponse(), status=status.HTTP_200_OK)
    #     else:
    #         return Response({'Update': 'Campos no valido'}, status=status.HTTP_200_OK)
    #
    # @action(methods=['post'], detail=False)
    # def DeleteNote(self, request):
    #     NoteDL = Note.objects.get(id=request.data.get('id'))
    #     NoteDL.delete()
    #     return Response('eliminado', status=status.HTTP_200_OK)