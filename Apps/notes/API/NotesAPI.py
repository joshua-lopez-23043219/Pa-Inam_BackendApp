from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.notes.API.SerializerNotes import SerializerNotes
from Apps.notes.models import Notes
from Apps.registrations.models import Registration


class NotesViewSet (ModelViewSet):

    queryset = Notes.objects.all()
    serializer_class = SerializerNotes

    # ========== LISTADO COMPLETO ==========
    @action(methods=['get'], detail=False, url_path='listar-notas')
    def listar_notas(self, request):
        notas = self.get_queryset()
        data = []

        for n in notas:
            reg = n.registration
            student = reg.student if reg else None
            subject = n.subject

            data.append({
                "registration_code": getattr(reg, "code_registration", None),
                "student": {
                    "code_student": getattr(student, "code_student", None),
                    "name_student": getattr(student, "name_student", None),
                    "surname_student": getattr(student, "surname_student", None),
                } if student else None,
                "subject": {
                    "code_subject": getattr(subject, "code_subject", None),
                    "name_subject": getattr(subject, "name_subject", None),
                } if subject else None,
                "first_partial": n.first_partial,
                "second_partial": n.second_partial,
                "first_semester": n.first_semester,
                "third_partial": n.third_partial,
                "quarter_partial": n.quarter_partial,
                "second_semester": n.second_semester,
                "final_grade": n.final_grade,
                "special_note": n.special_note,
            })

        return Response(data)

    # ========== BUSCAR NOTAS POR CÓDIGO DE MATRÍCULA ==========
    @action(methods=['get'], detail=False, url_path='buscar-por-codigo')
    def buscar_por_codigo(self, request):
        """
        /api/notes/buscar-por-codigo/?codigo=REG001
        """
        codigo = request.query_params.get('codigo')
        if not codigo:
            return Response(
                {"error": "Debes enviar el parámetro ?codigo= (code_registration)"},
                status=status.HTTP_400_BAD_REQUEST
            )

        reg = Registration.objects(code_registration=codigo).first()
        if not reg:
            return Response(
                {"error": "Matrícula no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        notas = Notes.objects(registration=reg).select_related()
        if not notas:
            return Response(
                {"message": "No hay notas para esa matrícula"},
                status=status.HTTP_200_OK
            )

        data = []
        for n in notas:
            subject = n.subject
            data.append({
                "registration_code": reg.code_registration,
                "subject": {
                    "code_subject": getattr(subject, "code_subject", None),
                    "name_subject": getattr(subject, "name_subject", None),
                } if subject else None,
                "first_partial": n.first_partial,
                "second_partial": n.second_partial,
                "first_semester": n.first_semester,
                "third_partial": n.third_partial,
                "quarter_partial": n.quarter_partial,
                "second_semester": n.second_semester,
                "final_grade": n.final_grade,
                "special_note": n.special_note,
            })

        return Response(data)