from typing import Any
from django import http
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.

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
        Profesional.objects.create(nombre=json_data['nombre'], rut=json_data['rut'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        json_data = json.loads(request.body)
        profesionales = list(Profesional.objects.filter(id=id).values())
        if len(profesionales)>0:
            profesional = Profesional.objects.get(id=id)
            profesional.nombre=json_data['nombre']
            profesional.rut=json_data['rut']
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
