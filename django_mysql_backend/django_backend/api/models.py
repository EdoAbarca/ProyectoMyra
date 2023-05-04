from django.db import models


# Create your models here.

class Cargo(models.Model):
    cargo = models.CharField(max_length=15)
    tipoContrato = models.CharField(max_length=15)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()


class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    #idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


class Pago(models.Model):
    monto = models.IntegerField()
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
