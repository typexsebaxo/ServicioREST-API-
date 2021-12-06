from django.contrib import admin
from django.utils.translation import ugettext

from registrapp_API.api.models import usuario
from .models import usuario

# Register your models here.

admin.site.register(usuario)