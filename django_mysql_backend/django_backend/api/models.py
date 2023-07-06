from django.db import models
# Create your models here.
    
##########################################################################

class Cargo(models.Model):
    cargo = models.CharField(max_length=15)

class Contrato(models.Model):
    tipoContrato = models.CharField(max_length=15)

class Centro(models.Model):
    nombreCentro = models.CharField(max_length=30)

class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    idCentro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Area(models.Model):
    nombreArea = models.CharField(max_length=30)

#llas estadisticas podrian ponerse en otra entidad para cada profesional
class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    #
    inasistencias = models.IntegerField()
    horasTotales = models.IntegerField()
    horasExtras = models.IntegerField()
    vacaciones = models.IntegerField()
    licencia = models.IntegerField()
    #
    idCentro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE)
    idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    idContrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    idCoordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)

class Pago(models.Model):
    sueldoBase = models.IntegerField()
    gratificacion = models.IntegerField()
    horaExtra = models.IntegerField()
    bonos = models.IntegerField()
    aguinaldo = models.IntegerField()
    vacaciones = models.IntegerField()
    viatico = models.IntegerField()
    asignacionFamiliar = models.IntegerField()
    colacion = models.IntegerField()
    movilizacion = models.IntegerField()
    salaCuna = models.IntegerField()
    totalHaberes = models.IntegerField()
    totalImponible = models.IntegerField()
    afp = models.IntegerField()
    isapre = models.IntegerField()
    fonasa = models.IntegerField()
    segCes = models.IntegerField()
    imptoUnico = models.IntegerField()
    ctaAfp = models.IntegerField()
    anticipos = models.IntegerField()
    descuento = models.IntegerField()
    ley3 = models.IntegerField()
    totalDescuento = models.IntegerField()
    liquido = models.IntegerField()
    fechaPago = models.DateField()
    idProfesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)

class Region(models.Model):
    nombreRegion = models.CharField(max_length=70)

class Zona(models.Model):
    nombreZona = models.CharField(max_length=70)

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=70)

class TipoTurno(models.Model):
    tipoTurno = models.CharField(max_length=10)

class Paciente(models.Model):
    #añadir cuidado
    #añadir gasto por paciente (sprint 3)
    nombre = models.CharField(max_length=70)
    fechaInicioAtencion = models.DateField()
    vigente = models.BooleanField()
    idZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTipoTurno = models.ForeignKey(TipoTurno, on_delete=models.CASCADE)

class Turno(models.Model):
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    horas = models.IntegerField()
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idProfesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)

class Asistencia(models.Model):
    fechaAsistencia = models.DateField()
    asisteProfesional = models.BooleanField()
    estado = models.IntegerField()
    idProfesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idTurno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    #idPago = models.ForeignKey(Pago, on_delete=models.CASCADE)

class Alerta(models.Model):
    #tipo = char
    #profesionales = lista o un solo profesional (id)
    fechaAlerta = models.DateField()
    descripcion = models.CharField(max_length=200)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idAsistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

