from django.test import TestCase
from api.models import *
import datetime

class Sprint1TestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Centro.objects.create(nombreCentro='Centro 1')
        Area.objects.create(nombreArea='Area 1')
        Profesional.objects.create(nombre='Nombre Ejemplo', rut='20237081-0', idCentro=Centro.objects.get(id=1),
                                   idArea=Area.objects.get(id=1))
        Asistencia.objects.create(fechaAsistencia=datetime.date(2023,6,1), asisteProfesional=True,
                                  estado=1, idProfesional=Profesional.objects.get(id=1))

    def test_nombre_max_length(self):
        profesional=Profesional.objects.get(id=1)
        max_length = profesional._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 50)

    def test_rut_max_length(self):
        profesional = Profesional.objects.get(id=1)
        max_length = profesional._meta.get_field('rut').max_length
        self.assertEquals(max_length, 15)

    def test_fechaAsistencia_valida(self):
        asistencia = Asistencia.objects.get(id=1)
        fecha = asistencia.fechaAsistencia
        if datetime.date.today() - datetime.timedelta(weeks=4) < fecha < datetime.date.today() + datetime.timedelta(weeks=4):
            self.assertTrue(True)
        else:
            self.assertTrue(False)