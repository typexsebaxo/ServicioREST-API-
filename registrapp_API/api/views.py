from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import usuario
import json
# Create your views here.

class vistausuario(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario=usuarios[0]
                datos={'message':"conseguido", 'usuarios':usuarios}
            else:
                datos={'message':"No se encuentra el usuario"}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':"conseguido", 'usuarios':usuarios}
            else:
                datos={'message':"No se encuentra el usuario"}
            return JsonResponse(datos)

    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        usuario.objects.create(nombre=jd['nombre'],clase=jd['clase'],asistencia=jd['asistencia'])
        datos={'message':"conseguido"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd=json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario=Usuario.objects.get(id=id)
                usuario.nombre=jd['nombre']
                usuario.clase=jd['clase']
                usuario.asistencia=jd['asistencia']
                usuario.save()
                datos={'message':"conseguido"}
            else:
                datos={'message':"No se encuentra el usuario"}
            return JsonResponse(datos)
        

    def delete(self,request):
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            Usuario.objects.filter(id=id).delete()
            datos={'message':"conseguido"}
        else:
            datos={'message':"No se encuentra el usuario"}
        return JsonResponse(datos)