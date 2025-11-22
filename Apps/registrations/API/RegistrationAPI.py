from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.registrations.API.SerializerRegistration import SerializerRegistration
from Apps.registrations.models import Registration


class RegistrationViewSet (ModelViewSet):

    queryset = Registration.objects.all()
    serializer_class = SerializerRegistration

    # ========== LISTADO COMPLETO (tipo reporte) ==========
    @action(methods=['get'], detail=False, url_path='listar-matriculas')
    def listar_matriculas(self, request):
        regs = self.get_queryset()
        data = []

        for r in regs:
            data.append({
                "code_registration": r.code_registration,
                "date_registration": r.date_registration,
                "mode_registration": r.mode_registration,
                "level_registration": r.level_registration,
                "student": {
                    "id": str(r.student.id) if r.student else None,
                    "code_student": getattr(r.student, "code_student", None),
                    "name_student": getattr(r.student, "name_student", None),
                    "surname_student": getattr(r.student, "surname_student", None),
                } if r.student else None,
                "group": {
                    "id": str(r.group.id) if r.group else None,
                    "code_group": getattr(r.group, "code_group", None),
                    "level_group": getattr(r.group, "level_group", None),
                    "section_group": getattr(r.group, "section_group", None),
                    "amount_group": getattr(r.group, "amount_group", None),
                } if r.group else None,
                "tutor": {
                    "id": str(r.tutor.id) if r.tutor else None,
                    "code_tutor": getattr(r.tutor, "code_tutor", None),
                    "name_tutor": getattr(r.tutor, "name_tutor", None),
                    "surname_tutor": getattr(r.tutor, "surname_tutor", None),
                    "phone_tutor": getattr(r.tutor, "phone_tutor", None),
                } if r.tutor else None,
            })

        return Response(data)

    # ========== BUSCAR POR CÓDIGO DE MATRÍCULA ==========
    @action(methods=['get'], detail=False, url_path='buscar-por-codigo')
    def buscar_por_codigo(self, request):
        codigo = request.query_params.get('codigo')
        if not codigo:
            return Response(
                {"error": "Debes enviar el parámetro ?codigo="},
                status=status.HTTP_400_BAD_REQUEST
            )

        r = Registration.objects(code_registration=codigo).select_related().first()
        if not r:
            return Response(
                {"error": "Matrícula no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
            "code_registration": r.code_registration,
            "date_registration": r.date_registration,
            "mode_registration": r.mode_registration,
            "level_registration": r.level_registration,
            "student": {
                "id": str(r.student.id) if r.student else None,
                "code_student": getattr(r.student, "code_student", None),
                "name_student": getattr(r.student, "name_student", None),
                "surname_student": getattr(r.student, "surname_student", None),
                "email_student": getattr(r.student, "email_student", None),
            } if r.student else None,
            "group": {
                "id": str(r.group.id) if r.group else None,
                "code_group": getattr(r.group, "code_group", None),
                "level_group": getattr(r.group, "level_group", None),
                "section_group": getattr(r.group, "section_group", None),
                "amount_group": getattr(r.group, "amount_group", None),
            } if r.group else None,
            "tutor": {
                "id": str(r.tutor.id) if r.tutor else None,
                "code_tutor": getattr(r.tutor, "code_tutor", None),
                "name_tutor": getattr(r.tutor, "name_tutor", None),
                "surname_tutor": getattr(r.tutor, "surname_tutor", None),
                "phone_tutor": getattr(r.tutor, "phone_tutor", None),
                "email_tutor": getattr(r.tutor, "email_tutor", None),
            } if r.tutor else None,
        }

        return Response(data)