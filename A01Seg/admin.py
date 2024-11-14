from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# ASIGNAMOS ROTULOS PARA EL CONTROL PANEL Y MÁS
admin.site.index_title  = 'OrderedMed'
admin.site.site_title   = 'Panel De Control'
admin.site.site_header  = 'PLATAFORMA PARA LA GESTIÓN DE CENTROS MÉDICOS'

# Register your models here.
admin.site.register(Isapre)
# admin.site.register(Usuario)
admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Funcionario)



