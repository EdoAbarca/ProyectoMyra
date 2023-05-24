from django.db import models


# Create your models here.

class Cargo(models.Model):
    cargo = models.CharField(max_length=15)
    tipoContrato = models.CharField(max_length=15)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()

class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    #idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    #idCoordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)


class Pago(models.Model):
    # añadir mas atributos de remuneraciones
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
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)


class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=70)


class Paciente(models.Model):
    nombre = models.CharField(max_length=70)
    rut = models.CharField(max_length=15)
    fechaInicioAtencion = models.DateField()
    vigente = models.BooleanField()
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Turno(models.Model):
    tipoTurno = models.CharField(max_length=10)
    fechaInicio = models.DateField()
    horaInicio = models.TimeField()
    fechaTermino = models.DateField()
    horaTermino = models.TimeField()
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idProfesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)


class Asistencia(models.Model):
    fechaEntrada = models.DateField()
    horaEntrada = models.TimeField()
    fechaSalida = models.DateField()
    horaSalida = models.TimeField()
    asisteProfesional = models.BooleanField()
    costosExtra = models.IntegerField()
    idProfesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    idTurno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    idPago = models.ForeignKey(Pago, on_delete=models.CASCADE)


class Alerta(models.Model):
    fechaAlerta = models.DateField()
    descripcion = models.CharField(max_length=200)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idAsistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

class Excel(models.Model):
    #probar con un filefield quizas
    data = models.CharField(max_length=255)