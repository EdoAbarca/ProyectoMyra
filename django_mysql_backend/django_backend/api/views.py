from typing import Any
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
class CargoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            cargos = list(Cargo.objects.filter(id=id).values())
            if len(cargos)>0:
                cargo = cargos[0]
                datos = {'message': "Success", 'cargo':cargo}
            else:
                datos = {'message': "Cargo no encontrado."}
            return JsonResponse(datos)
        else:
            cargos = list(Cargo.objects.values())
            if len(cargos)>0:
                datos = {'message': "Success", 'cargos':cargos}
            else:
                datos = {'message': "Sin cargos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Cargo.objects.create(cargo=json_data['cargo'], tipoContrato=json_data['tipoContrato'],
                             fechaInicio=json_data['fechaInicio'], fechaTermino=json_data['fechaTermino'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        cargos = list(Cargo.objects.filter(id=id).values())
        if len(cargos)>0:
            cargos = Cargo.objects.get(id=id)
            cargos.cargos=json_data['cargos']
            cargos.tipoContrato=json_data['tipoContrato']
            cargos.fechaInicio=json_data['fechaInicio']
            cargos.fechaTermino=json_data['fechaTermino']
            cargos.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Cargo no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        cargos = list(Cargo.objects.filter(id=id).values())
        if len(cargos) > 0:
            Cargo.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Cargo no encontrado"}
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
        Coordinador.objects.create(nombre=json_data['nombre'], idCargo=json_data['idCargo'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        coordinadores = list(Coordinador.objects.filter(id=id).values())
        if len(coordinadores) > 0:
            coordinador = Coordinador.objects.get(id=id)
            coordinador.nombre = json_data['nombre']
            coordinador.idCargo = json_data['idCargo']
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

class ProfesionalView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            profesionales = list(Profesional.objects.filter(id=id).values())
            if len(profesionales)>0:
                profesional = profesionales[0]
                datos = {'message': "Success", 'profesional':profesional}
            else:
                datos = {'message': "Profesional no encontrado."}
            return JsonResponse(datos)
        else:
            profesionales = list(Profesional.objects.values())
            if len(profesionales)>0:
                datos = {'message': "Success", 'profesionales':profesionales}
            else:
                #datos = {'message': "Sin profesionales.", 'profesionales':[]}
                datos = {'message': "Sin profesionales."}
            return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        Profesional.objects.create(nombre=json_data['nombre'], rut=json_data['rut'], idCargo=json_data['idCargo'],
                                   idCoordinador=json_data['idCoordinador'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        json_data = json.loads(request.body)
        profesionales = list(Profesional.objects.filter(id=id).values())
        if len(profesionales)>0:
            profesional = Profesional.objects.get(id=id)
            profesional.nombre=json_data['nombre']
            profesional.rut=json_data['rut']
            profesional.idCargo=json_data['idCargo']
            profesional.idCoordinador=json_data['idCoordinador']
            profesional.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Profesional no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        profesionales = list(Profesional.objects.filter(id=id).values())
        if len(profesionales) > 0:
            Profesional.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Profesional no encontrado"}
        return JsonResponse(datos)
    
    #Por hacer:
    '''
    def getSearch(self, request, search):
        profesionales = list(Profesional.objects.filter(id=id).values()) #aqui se hace el filtro por lo ingresado en la barra de busqueda
        if len(profesionales)>0:
            datos = {'message': "Success", 'profesionales':profesionales}
        else:
            datos = {'message': "No hay coincidencias."}
        return JsonResponse(datos)

    '''
class PagoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            pagos = list(Pago.objects.filter(id=id).values())
            if len(pagos)>0:
                pago = pagos[0]
                datos = {'message': "Success", 'pago': pago}
            else:
                datos = {'message': "Pago no encontrado."}
            return JsonResponse(datos)
        else:
            pagos = list(Pago.objects.values())
            if len(pagos)>0:
                datos = {'message': "Success", 'pagos': pagos}
            else:
                datos = {'message': "Sin pagos."}
            return JsonResponse(datos)

    def post(self, request):
        json_data = json.loads(request.body)
        Pago.objects.create(monto=json_data['monto'], fechaPago=json_data['fechaPago'],
                            idProfesional=json_data['idProfesional'])
        datos = {'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        pagos = list(Pago.objects.filter(id=id).values())
        if len(pagos)>0:
            pagos = Pago.objects.get(id=id)
            pagos.monto=json_data['monto']
            pagos.fechaPago=json_data['fechaPago']
            pagos.idProfesional=json_data['idProfesional']
            pagos.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Pago no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        pagos = list(Pago.objects.filter(id=id).values())
        if len(pagos) > 0:
            Pago.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Pago no encontrado"}
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
        Zona.objects.create(nombreZona=json_data['nombreZona'], idRegion=json_data['idRegion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        json_data = json.loads(request.body)
        zonas = list(Zona.objects.filter(id=id).values())
        if len(zonas) > 0:
            zonas = Zona.objects.get(id=id)
            zonas.nombreZona = json_data['nombreZona']
            zonas.idRegion = json_data['idRegion']
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

#Adaptar con pandas
class ExcelView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    @login_required
    def cargar_excel(self, request):
        if request.method == 'POST':
            file = request.FILES['excel_file']
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                #Crear elementos y mandar a BD
                print(index+row)
    
@csrf_exempt 
def signup(self, request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeatPassword']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email= request.POST['email'])
                user.save()
                datos = {'message': "Success"}
            except:
                datos = {'message': "Usuario ya está en uso"}
        datos = {'message': "Contraseñas no coinciden"}
    datos = {'message': "GET request: "+request}
    return JsonResponse(datos)

@csrf_exempt 
def signin(self, request):
    if request.method == 'POST':
        user = authenticate(request, email=request.POST['email'], password = request.POST['password'])
        if user is None:
            datos = {'message': "Error con credenciales"}
        else:
            login(request, user)
            datos = {'message': "Success"}
        return JsonResponse(datos)

@csrf_exempt 
@login_required
def signout(self, request):
    logout(request)
    datos = {'message': "Success"}
    return JsonResponse(datos)
