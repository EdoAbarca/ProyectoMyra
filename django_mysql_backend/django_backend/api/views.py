from typing import Any
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views import View  # A cambiar
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import pandas as pd
#from django.contrib.auth import login, logout
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.parsers import MultiPartParser


#############################################################################################
#############################################################################################
#############################################################################################

# CRUD

class CargoView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, id=0):
        try:
            if (id > 0):
                cargo = Cargo.objects.get(id=id)
                serializer = CargoSerializer(cargo)
                data = {"message": "Success", "cargo": serializer.data}
                return Response(data, status=status.HTTP_200_OK)
            else:
                cargos = Cargo.objects.all()
                serializer = CargoSerializer(cargos, many=True)
                data = {"message": "Success", "cargos": serializer.data}
                return Response(data, status=status.HTTP_200_OK)
        except Exception as error:
            data = {"message": "Error: "+str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
    def post(self, request):
        try:
            serializer = CargoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {"message": "Success"}
                return Response(data, status=status.HTTP_201_CREATED)
            data = {"message": "Error: "+serializer.errors.__str__()}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            data = {"message": "Error: "+str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            cargo = Cargo.objects.get(id=id)
            if cargo is not None:
                serializer = CargoSerializer(cargo, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            data = {"message": "Error: "+str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            cargo = Cargo.objects.get(id=id)
            if cargo is not None:
                cargo.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            data = {"message": "Error: "+str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class ContratoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            contratos = list(Contrato.objects.filter(id=id).values())
            if len(contratos) > 0:
                contrato = contratos[0]
                datos = {'message': "Success", 'contrato': contrato}
            else:
                datos = {'message': "Contrato no encontrado."}
            return JsonResponse(datos)
        else:
            contratos = list(Contrato.objects.values())
            if len(contratos) > 0:
                datos = {'message': "Success", 'contratos': contratos}
            else:
                datos = {'message': "Sin contratos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Contrato.objects.create(tipoContrato=json_data['tipoContrato'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        contratos = list(Contrato.objects.filter(id=id).values())
        if len(contratos) > 0:
            contratos = Contrato.objects.get(id=id)
            contratos.tipoContrato = json_data['tipoContrato']
            contratos.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Contrato no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        contratos = list(Contrato.objects.filter(id=id).values())
        if len(contratos) > 0:
            Contrato.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Contrato no encontrado"}
        return JsonResponse(datos)


class CentroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            centros = list(Centro.objects.filter(id=id).values())
            if len(centros) > 0:
                centro = centros[0]
                datos = {'message': "Success", 'centro': centro}
            else:
                datos = {'message': "Centro no encontrado."}
            return JsonResponse(datos)
        else:
            centros = list(Centro.objects.values())
            if len(centros) > 0:
                datos = {'message': "Success", 'centros': centros}
            else:
                datos = {'message': "Sin centros."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Centro.objects.create(nombreCentro=json_data['nombreCentro'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        centros = list(Centro.objects.filter(id=id).values())
        if len(centros) > 0:
            centros = Centro.objects.get(id=id)
            centros.nombreCentro = json_data['nombreCentro']
            centros.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Centro no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        centros = list(Centro.objects.filter(id=id).values())
        if len(centros) > 0:
            Centro.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Centro no encontrado"}
        return JsonResponse(datos)


class CoordinadorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            coordinadores = list(Coordinador.objects.filter(id=id).values())
            if len(coordinadores) > 0:
                coordinador = coordinadores[0]
                datos = {'message': "Success", 'coordinador': coordinador}
            else:
                datos = {'message': "Coordinador no encontrado."}
            return JsonResponse(datos)
        else:
            coordinadores = list(Coordinador.objects.values())
            if len(coordinadores) > 0:
                datos = {'message': "Success", 'coordinadores': coordinadores}
            else:
                datos = {'message': "Sin coordinadores."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Coordinador.objects.create(nombre=json_data['nombre'], rut=json_data['rut'], idCargo=json_data['idCargo'],
                                   idCentro=json_data['idCentro'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        coordinadores = list(Coordinador.objects.filter(id=id).values())
        if len(coordinadores) > 0:
            coordinador = Coordinador.objects.get(id=id)
            coordinador.nombre = json_data['nombre']
            coordinador.rut = json_data['rut']
            coordinador.idCargo = json_data['idCargo']
            coordinador.idCentro = json_data['idCentro']
            coordinador.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Coordinador no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        coordinadores = list(Coordinador.objects.filter(id=id).values())
        if len(coordinadores) > 0:
            Coordinador.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Coordinador no encontrado"}
        return JsonResponse(datos)


class AreaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            areas = list(Area.objects.filter(id=id).values())
            if len(areas) > 0:
                area = areas[0]
                datos = {'message': "Success", 'area': area}
            else:
                datos = {'message': "Area no encontrada."}
            return JsonResponse(datos)
        else:
            areas = list(Area.objects.values())
            if len(areas) > 0:
                datos = {'message': "Success", 'areas': areas}
            else:
                datos = {'message': "Sin areas."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Area.objects.create(nombreArea=json_data['nombreArea'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            areas = Area.objects.get(id=id)
            areas.nombreArea = json_data['nombreArea']
            areas.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Area no encontrada"}
        return JsonResponse(datos)

    def delete(self, request, id):
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            Area.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Area no encontrada"}
        return JsonResponse(datos)


class ProfesionalView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            try:
                profesional = Profesional.objects.get(id=id)
            except Profesional.DoesNotExist:
                datos = {'message': 'Profesional no encontrado'}
                return JsonResponse(datos, status=404)

            
            pagos = Pago.objects.filter(idProfesional_id=id)
            asistencias = Asistencia.objects.filter(idProfesional_id=id)

            datos_profesional = {
                'nombre': profesional.nombre,
                'rut': profesional.rut,
                'inasistencias': profesional.inasistencias,
                'horasTotales': profesional.horasTotales,
                'horasExtras': profesional.horasExtras,
                'vacaciones': profesional.vacaciones,
                'licencia': profesional.licencia,
                'idCentro_id': profesional.idCentro.id,
                'idArea_id': profesional.idArea.id,
                'idCargo_id': profesional.idCargo.id,
                'idContrato_id': profesional.idContrato.id,
                'tipoContrato': profesional.idContrato.tipoContrato,
                'idCoordinador_id': profesional.idCoordinador.id,
                'nombreCoordinador': profesional.idCoordinador.nombre,
                'asistencias': [
                    {'id': asistencia.id, 'fechaAsistencia': asistencia.fechaAsistencia, 'asisteProfesional': asistencia.asisteProfesional,
                     'estado': asistencia.estado, 'nombrePaciente': asistencia.idPaciente.nombre,
                     'idTurno_id': asistencia.idTurno.id} for asistencia in asistencias],
                'pagos': [
                    {'sueldoBase': pago.sueldoBase, 'gratificacion': pago.gratificacion, 'horaExtra': pago.horaExtra,
                     'bonos': pago.bonos, 'aguinaldo': pago.aguinaldo, 'vacaciones': pago.vacaciones,
                     'viatico': pago.viatico, 'asignacionFamiliar': pago.asignacionFamiliar,
                     'colacion': pago.colacion, 'movilizacion': pago.movilizacion, 'salaCuna': pago.salaCuna,
                     'totalHaberes': pago.totalHaberes, 'totalImponible': pago.totalImponible, 'afp': pago.afp,
                     'isapre': pago.isapre, 'fonasa': pago.fonasa, 'segCes': pago.segCes,
                     'imptoUnico': pago.imptoUnico, 'ctaAfp': pago.ctaAfp, 'anticipos': pago.anticipos,
                     'descuento': pago.descuento, 'ley3': pago.ley3, 'totalDescuento': pago.totalDescuento,
                     'liquido': pago.liquido, 'fechaPago': pago.fechaPago} for pago in pagos],
            }

            datos = {'message': 'Success', 'profesional': datos_profesional}
            return JsonResponse(datos)
        else:
            profesionales = list(Profesional.objects.values())
            if len(profesionales) > 0:
                datos = {'message': "Success", 'profesionales': profesionales}
            else:
                datos = {'message': "Sin profesionales."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Profesional.objects.create(nombre=json_data['nombre'], rut=json_data['rut'], inasistencias=json_data['inasistencias'],
                                   horasTotales=json_data['horasTotales'], horasExtras=json_data['horasExtras'],
                                   vacaciones=json_data['vacaiones'], licencia=json_data['licencia'],
                                   idCentro=json_data['idCentro'], idArea=['idArea'], idCargo=json_data['idCargo'],
                                   idContrato=json_data['idContrato'], idCoordinador=json_data['idCoordinador'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        profesionales = list(Profesional.objects.filter(id=id).values())
        if len(profesionales) > 0:
            profesional = Profesional.objects.get(id=id)
            profesional.nombre = json_data['nombre']
            profesional.rut = json_data['rut']
            profesional.inasistencias = json_data['inasistencias']
            profesional.horasTotales = json_data['horasTotales']
            profesional.horasExtras = json_data['horasExtras']
            profesional.vacaciones = json_data['vacaiones']
            profesional.licencia = json_data['licencia']
            profesional.idCentro = json_data['idCentro']
            profesional.idArea = json_data['idArea']
            profesional.idCargo = json_data['idCargo']
            profesional.idContrato = json_data['idContrato']
            profesional.idCoordinador = json_data['idCoordinador']
            profesional.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Profesional no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        profesionales = list(Profesional.objects.filter(id=id).values())
        if len(profesionales) > 0:
            Profesional.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Profesional no encontrado"}
        return JsonResponse(datos)


class PagoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            pagos = list(Pago.objects.filter(id=id).values())
            if len(pagos) > 0:
                pago = pagos[0]
                datos = {'message': "Success", 'pago': pago}
            else:
                datos = {'message': "Pago no encontrado."}
            return JsonResponse(datos)
        else:
            pagos = list(Pago.objects.values())
            if len(pagos) > 0:
                datos = {'message': "Success", 'pagos': pagos}
            else:
                datos = {'message': "Sin pagos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Pago.objects.create(sueldoBase=json_data['sueldoBase'], gratificacion=json_data['gratificacion'],
                            horaExtra=json_data['horaExtra'], bonos=json_data['bonos'],
                            aguinaldo=json_data['aguinaldo'], vacaciones=json_data['vacaciones'],
                            viatico=json_data['viatico'], asignacionFamiliar=json_data['asignacionFamiliar'],
                            colacion=json_data['colacion'], movilizacion=json_data['movilizacion'],
                            salaCuna=json_data['salaCuna'], totalHaberes=json_data['totalHaberes'],
                            totalImponible=json_data['totalImponible'], afp=json_data['afp'],
                            isapre=json_data['isapre'], fonasa=json_data['fonasa'], segCes=json_data['segCes'],
                            imptoUnico=json_data['imptoUnico'], ctaAfp=json_data['ctaAfp'],
                            anticipos=json_data['anticipos'], descuento=json_data['descuento'], ley3=json_data['ley3'],
                            totalDescuento=json_data['totalDescuento'], liquido=json_data['liquido'],
                            fechaPago=json_data['fechaPago'],
                            idProfesional=json_data['idProfesional'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        pagos = list(Pago.objects.filter(id=id).values())
        if len(pagos) > 0:
            pagos = Pago.objects.get(id=id)
            pagos.sueldoBase = json_data['sueldoBase']
            pagos.gratificacion = json_data['gratificacion']
            pagos.horaExtra = json_data['horaExtra']
            pagos.bonos = json_data['bonos']
            pagos.aguinaldo = json_data['aguinaldo']
            pagos.vacaciones = json_data['vacaciones']
            pagos.viatico = json_data['viatico']
            pagos.asignacionFamiliar = json_data['asignacionFamiliar']
            pagos.colacion = json_data['colacion']
            pagos.movilizacion = json_data['movilizacion']
            pagos.salaCuna = json_data['salaCuna']
            pagos.totalHaberes = json_data['totalHaberes']
            pagos.totalImponible = json_data['totalImponible']
            pagos.afp = json_data['afp']
            pagos.isapre = json_data['isapre']
            pagos.fonasa = json_data['fonasa']
            pagos.segCes = json_data['segCes']
            pagos.imptoUnico = json_data['imptoUnico']
            pagos.ctaAfp = json_data['ctaAfp']
            pagos.anticipos = json_data['anticipos']
            pagos.descuento = json_data['descuento']
            pagos.ley3 = json_data['ley3']
            pagos.totalDescuento = json_data['totalDescuento']
            pagos.liquido = json_data['liquido']
            pagos.fechaPago = json_data['fechaPago']
            pagos.idProfesional = json_data['idProfesional']
            pagos.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Pago no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        pagos = list(Pago.objects.filter(id=id).values())
        if len(pagos) > 0:
            Pago.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Pago no encontrado"}
        return JsonResponse(datos)


class RegionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            regiones = list(Region.objects.filter(id=id).values())
            if len(regiones) > 0:
                region = regiones[0]
                datos = {'message': "Success", 'region': region}
            else:
                datos = {'message': "Region no encontrada."}
            return JsonResponse(datos)
        else:
            regiones = list(Region.objects.values())
            if len(regiones) > 0:
                datos = {'message': "Success", 'regiones': regiones}
            else:
                datos = {'message': "Sin regiones."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Region.objects.create(nombreRegion=json_data['nombreRegion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        regiones = list(Region.objects.filter(id=id).values())
        if len(regiones) > 0:
            regiones = Region.objects.get(id=id)
            regiones.nombreRegion = json_data['nombreRegion']
            regiones.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Region no encontrada"}
        return JsonResponse(datos)

    def delete(self, request, id):
        regiones = list(Region.objects.filter(id=id).values())
        if len(regiones) > 0:
            Region.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Region no encontrada"}
        return JsonResponse(datos)


class ZonaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            zonas = list(Zona.objects.filter(id=id).values())
            if len(zonas) > 0:
                zona = zonas[0]
                datos = {'message': "Success", 'zona': zona}
            else:
                datos = {'message': "Zona no encontrada."}
            return JsonResponse(datos)
        else:
            zonas = list(Zona.objects.values())
            if len(zonas) > 0:
                datos = {'message': "Success", 'zonas': zonas}
            else:
                datos = {'message': "Sin zonas."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Zona.objects.create(nombreZona=json_data['nombreZona'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        zonas = list(Zona.objects.filter(id=id).values())
        if len(zonas) > 0:
            zonas = Zona.objects.get(id=id)
            zonas.nombreZona = json_data['nombreZona']
            zonas.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Zona no encontrada"}
        return JsonResponse(datos)

    def delete(self, request, id):
        zonas = list(Zona.objects.filter(id=id).values())
        if len(zonas) > 0:
            Zona.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Zona no encontrada"}
        return JsonResponse(datos)


class ClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            clientes = list(Cliente.objects.filter(id=id).values())
            if len(clientes) > 0:
                cliente = clientes[0]
                datos = {'message': "Success", 'cliente': cliente}
            else:
                datos = {'message': "Cliente no encontrado."}
            return JsonResponse(datos)
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = {'message': "Success", 'clientes': clientes}
            else:
                datos = {'message': "Sin clientes."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Cliente.objects.create(nombreCliente=json_data['nombreCliente'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        clientes = list(Cliente.objects.filter(id=id).values())
        if len(clientes) > 0:
            clientes = Cliente.objects.get(id=id)
            clientes.nombreCliente = json_data['nombreCliente']
            clientes.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Cliente no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        clientes = list(Cliente.objects.filter(id=id).values())
        if len(clientes) > 0:
            Cliente.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Cliente no encontrado"}
        return JsonResponse(datos)


class TipoTurnoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            tipoturnos = list(TipoTurno.objects.filter(id=id).values())
            if len(tipoturnos) > 0:
                tipoturno = tipoturnos[0]
                datos = {'message': "Success", 'tipoturno': tipoturno}
            else:
                datos = {'message': "Tipo turno no encontrado."}
            return JsonResponse(datos)
        else:
            tipoturnos = list(TipoTurno.objects.values())
            if len(tipoturnos) > 0:
                datos = {'message': "Success", 'tipoturnos': tipoturnos}
            else:
                datos = {'message': "Sin tipo turnos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        TipoTurno.objects.create(tipoTurno=json_data['tipoTurno'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        tipoturnos = list(TipoTurno.objects.filter(id=id).values())
        if len(tipoturnos) > 0:
            tipoturno = TipoTurno.objects.get(id=id)
            tipoturno.tipoTurno = json_data['cargo']
            tipoturno.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipo turno no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        tipoturnos = list(TipoTurno.objects.filter(id=id).values())
        if len(tipoturnos) > 0:
            TipoTurno.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Tipo turno no encontrado"}
        return JsonResponse(datos)


class PacienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            try:
                paciente = Paciente.objects.get(id=id)
            except Paciente.DoesNotExist:
                datos = {'message': 'Profesional no encontrado'}
                return JsonResponse(datos, status=404)

            datos_asistencias = []
            asistencias = Asistencia.objects.filter(idPaciente_id=id)
            for asistencia in asistencias:
                datos_asistencia = {
                    'id': asistencia.id,
                    'fechaAsistencia': asistencia.fechaAsistencia,
                    'asisteProfesional': asistencia.asisteProfesional,
                    'estado': asistencia.estado,
                    'idTurno_id': asistencia.idTurno.id,
                    'nombreProfesional': asistencia.idProfesional.nombre,
                    'rutProfesional': asistencia.idProfesional.rut,
                    'idArea_id': asistencia.idProfesional.idArea.id
                }
                datos_asistencias.append(datos_asistencia)

            datos_paciente = {
                'nombre': paciente.nombre,
                'tipoTurno': paciente.tipoTurno,
                'fechaInicioAtencion': paciente.fechaInicioAtencion,
                'vigente': paciente.vigente,
                'idZona_id': paciente.idZona.id,
                'idRegion_id': paciente.idRegion.id,
                'idCliente_id': paciente.idCliente.id,
                'idTipoTurno': paciente.idTipoTurno.id,
                'asistencias': datos_asistencias,
                'zona': paciente.idZona.nombreZona,
                'region': paciente.idRegion.nombreRegion
            }

            datos = {'message': 'Success', 'paciente': datos_paciente}
            return JsonResponse(datos)
        else:
            pacientes = list(Paciente.objects.values())
            if len(pacientes) > 0:
                datos = {'message': "Success", 'pacientes': pacientes}
            else:
                datos = {'message': "Sin pacientes."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Paciente.objects.create(nombre=json_data['nombre'],
                                fechaInicioAtencion=json_data['fechaInicioAtencion'],
                                vigente=json_data['vigente'], idZona=json_data['idZona'], idRegion=json_data['idRegion'],
                                idCliente=json_data['idCliente'], idTipoTurno=json_data['idTipoTurno'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        pacientes = list(Paciente.objects.filter(id=id).values())
        if len(pacientes) > 0:
            paciente = Paciente.objects.get(id=id)
            paciente.nombre = json_data['nombre']
            paciente.fechaInicioAtencion = json_data['fechaInicioAtencion']
            paciente.vigente = json_data['vigente']
            paciente.idZona = json_data['idZona']
            paciente.idRegion = json_data['idRegion']
            paciente.idCliente = json_data['idCliente']
            paciente.idTipoTurno = json_data['idTipoTurno']
            paciente.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Paciente no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        pacientes = list(Paciente.objects.filter(id=id).values())
        if len(pacientes) > 0:
            Paciente.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Paciente no encontrado"}
        return JsonResponse(datos)


class TurnoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            turnos = list(Turno.objects.filter(id=id).values())
            if len(turnos) > 0:
                turno = turnos[0]
                datos = {'message': "Success", 'turno': turno}
            else:
                datos = {'message': "Turno no encontrado."}
            return JsonResponse(datos)
        else:
            turnos = list(Turno.objects.values())
            if len(turnos) > 0:
                datos = {'message': "Success", 'turnos': turnos}
            else:
                datos = {'message': "Sin turnos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Turno.objects.create(fechaInicio=json_data['fechaInicio'],
                             fechaTermino=json_data['fechaTermino'], horas=json_data['horas'],
                             idPaciente=json_data['idPaciente'], idProfesional=json_data['idProfesional'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        turnos = list(Turno.objects.filter(id=id).values())
        if len(turnos) > 0:
            turnos = Turno.objects.get(id=id)
            turnos.fechaInicio = json_data['fechaInicio']
            turnos.fechaTermino = json_data['fechaTermino']
            turnos.horas = json_data['horas']
            turnos.idPaciente = json_data['idPaciente']
            turnos.idProfesional = json_data['idProfesional']
            turnos.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Turno no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        turnos = list(Turno.objects.filter(id=id).values())
        if len(turnos) > 0:
            Turno.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Turno no encontrado"}
        return JsonResponse(datos)


class AsistenciaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            asistencias = list(Asistencia.objects.filter(id=id).values())
            if len(asistencias) > 0:
                asistencia = asistencias[0]
                datos = {'message': "Success", 'asistencia': asistencia}
            else:
                datos = {'message': "Asistencia no encontrada"}
            return JsonResponse(datos)
        else:
            asistencias = list(Asistencia.objects.values())
            if len(asistencias) > 0:
                datos = {'message': "Success", 'asistencias': asistencias}
            else:
                datos = {'message': "Sin asistencias"}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Asistencia.objects.create(fechaAsistencia=json_data['fechaAsistencia'],
                                  asisteProfesional=json_data['asisteProfesional'], estado=json_data['estado'],
                                  idProfesional=json_data['idProfesional'], idPaciente=json_data['idPaciente'],
                                  idTurno=json_data['idTurno'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        asistencias = list(Asistencia.objects.filter(id=id).values())
        if len(asistencias) > 0:
            asistencias = Asistencia.objects.get(id=id)
            asistencias.fechaAsistencia = json_data['fechaAsistencia']
            asistencias.asisteProfesional = json_data['asisteProfesional']
            asistencias.estado = json_data['estado']
            asistencias.idProfesional = json_data['idProfesional']
            asistencias.idPaciente = json_data['idPaciente']
            asistencias.idTurno = json_data['idTurno']
            asistencias.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Asistencia no encontrada."}
        return JsonResponse(datos)

    def delete(self, request, id):
        asistencias = list(Asistencia.objects.filter(id=id).values())
        if len(asistencias) > 0:
            Asistencia.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Asistenciano encontrada"}
        return JsonResponse(datos)


#############################################################################################
#############################################################################################
#############################################################################################

# FUNCIONALIDADES

class SearchView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        query = request.GET.get('query', '')
        profesionales = Profesional.objects.filter(
            Q(nombre__icontains=query) | Q(rut__icontains=query)
        ).values()

        if profesionales.exists:
            datos = {'message': 'Success',
                     'profesionales': list(profesionales)}
        else:
            datos = {'message': 'No se encontraron coincidencias'}

        return JsonResponse(datos)


class FilterAreaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_area=0):
        profesionales = Profesional.objects.filter(idArea_id=id_area)

        datos_profesionales = []

        for profesional in profesionales:
            datos_profesional = {
                'id': profesional.id,
                'nombre': profesional.nombre,
                'rut': profesional.rut,
                'idCentro_id': profesional.idCentro.id,
                'idArea_id': profesional.idArea.id,
                'idCargo_id': profesional.idCargo.id,
                # 'idCoordinador': profesional.idCoordinador.id,
            }

            datos_profesionales.append(datos_profesional)

        datos = {'message': 'Success', 'profesionales': datos_profesionales}
        return JsonResponse(datos)


class FilterCenterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_centro):
        profesionales = Profesional.objects.filter(idCentro_id=id_centro)

        datos_profesionales = []

        for profesional in profesionales:
            datos_profesional = {
                'id': profesional.id,
                'nombre': profesional.nombre,
                'rut': profesional.rut,
                'idCentro_id': profesional.idCentro.id,
                'idArea_id': profesional.idArea.id,
                'idCargo_id': profesional.idCargo.id,
                # 'idCoordinador': profesional.idCoordinador.id,
            }

            datos_profesionales.append(datos_profesional)

        datos = {'message': 'Success', 'profesionales': datos_profesionales}
        return JsonResponse(datos)


class SearchPacienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        query = request.GET.get('query', '')
        pacientes = Paciente.objects.filter(
            Q(nombre__icontains=query) | Q(rut__icontains=query)
        ).values()

        if pacientes.exists:
            datos = {'message': 'Success', 'pacientes': list(pacientes)}
        else:
            datos = {'message': 'No se encontraron coincidencias'}

        return JsonResponse(datos)


class FilterTipoClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_cliente=0):
        pacientes = Paciente.objects.filter(idCliente_id=id_cliente)

        datos_pacientes = []

        for paciente in pacientes:
            datos_paciente = {
                'id': paciente.id,
                'nombre': paciente.nombre,
                'rut': paciente.rut,
                'tipoTurno': paciente.tipoTurno,
                'fechaInicioAtencion': paciente.fechaInicioAtencion,
                'vigente': paciente.vigente,
                'idZona_id': paciente.idZona.id,
                'idRegion_id': paciente.idRegion.id,
                'idCliente_id': paciente.idCliente.id,
            }

            datos_pacientes.append(datos_paciente)

        datos = {'message': 'Success', 'pacientes': datos_pacientes}
        return JsonResponse(datos)


class FilterTipoTurnoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_turno=0):
        pacientes = Paciente.objects.filter(idTurno_id=id_turno)

        datos_pacientes = []

        for paciente in pacientes:
            datos_paciente = {
                'id': paciente.id,
                'nombre': paciente.nombre,
                'rut': paciente.rut,
                'tipoTurno': paciente.tipoTurno,
                'fechaInicioAtencion': paciente.fechaInicioAtencion,
                'vigente': paciente.vigente,
                'idZona_id': paciente.idZona.id,
                'idRegion_id': paciente.idRegion.id,
                'idCliente_id': paciente.idCliente.id,
            }

            datos_pacientes.append(datos_paciente)

        datos = {'message': 'Success', 'pacientes': datos_pacientes}
        return JsonResponse(datos)


class CargaExcelView(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            title = request.POST.get('title')
            print(title)
            date = request.POST.get('date')
            print(date)
            file = request.FILES['excel']
            print(file.name)
            df = pd.read_excel(file, sheet_name=2)
            # df = pd.read_excel(file)
            print(df)
            # for index, row in df.iterrows():
            datos = {'message': 'success'}
            return Response(datos, status=status.HTTP_201_CREATED)
        except:
            datos = {'message': 'fail'}
            return Response(datos, status=status.HTTP_409_CONFLICT)


class ReporteProfesionalView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_profesional):
        try:
            profesional = list(Profesional.objects.filter(
                id=id_profesional).values())
            datos = {'message': 'success', 'data': profesional}
            return JsonResponse(datos, status=200)
        except Profesional.DoesNotExist or not (id_profesional.isdigit()) or id_profesional <= 0:
            datos = {'message': 'fail'}
            return JsonResponse(datos, status=404)


#############################################################################################
#############################################################################################
#############################################################################################

# USUARIO
'''
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        #clean_data = custom_validation(request.data)
        clean_data = request.data
        try:
            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create(clean_data)
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            data = {'Error': str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        try:
            #assert validate_email(data)
            #assert validate_password(data)
            serializer = UserLoginSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.check_credentials(data)
                print(user)
                if user:
                    serializer = CustomTokenObtainPairSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        return Response({'message':'Success', 'data': serializer.validated_data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as error:
            data = {'Error': str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            

class UserLogout(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (SessionAuthentication,)

    def post(self, request):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as error:
            data = {'Error': str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            data = {'Error': str(error),'user': 'No hay sesión iniciada'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

'''

from rest_framework_simplejwt.tokens import RefreshToken
class UserRegister(APIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (permissions.AllowAny,)
    #serializer_class = serializers.UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)

class UserLogin(APIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (permissions.AllowAny,)
    #serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            print(user)
            storedUser = User.objects.get(email=user['email'])
            #serializer = serializers.CustomUserSerializer(user)
            print(storedUser)
            token = RefreshToken.for_user(storedUser)
            #data = serializer.data
            data = {"refresh": str(token), "access": str(token.access_token)}
            print(data)
            #login(request, user)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as error:
            data = {'Error': str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            print("Token a mandar a blacklist:", token)
            token.blacklist()
            #logout(request)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as error:
            data = {'Error': str(error)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    """
    Get, Update user information
    """

    permission_classes = (permissions.AllowAny,)
    #serializer_class = serializers.CustomUserSerializer

    def get(self, request):
        try:
            print(request)
            #print(request.data)
            print(request.user)
            serializer = UserSerializer(request.user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            data = {'Error': str(error),'user': 'No hay sesión iniciada'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
