from django.urls import path
from .views import vistausuario

urlpatterns=[
    path('usuarios/',vistausuario.as_view(),name='nompre_usuarios')
    path('usuarios/<int:id>',vistausuario.as_view(),name='lista_usuarios')
]