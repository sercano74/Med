from django.db import models
from django.contrib.auth.models import User, Group,Permission
from django.contrib.auth.models import Group

from django.utils.html import format_html
from OrderedMed.settings import STATIC_ROOT, MEDIA_ROOT
from django.db.models.signals import post_save

from datetime import date


class Isapre(models.Model):
    name    = models.CharField(max_length=100,null=True, blank=True)
    class Meta:
        verbose_name = 'Isapre'
        verbose_name_plural = 'Isapres'
        ordering = ['name']
    def __str__(self):
        return f'{self.name}'



class Medico(models.Model):
    user        = models.OneToOneField(User, on_delete=models.RESTRICT,related_name='medicos', verbose_name='Médico',help_text='Usuario con perfil de médico')
    image       = models.ImageField(default='/img_no_disp.png',upload_to="usuarios")
    dni         = models.CharField(max_length=10, null=True,blank=True)
    nacim       = models.DateField(blank=True, null=True)
    phone       = models.CharField(max_length=12,null=True, blank=True)
    especialidad    = models.CharField(max_length=100)
    experiencia     = models.TextField(max_length=500,null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, null=True)
    estados     = (('0','No activo'),('1','Activo'),('2','Vacaciones'))
    estado      = models.CharField(max_length=20,choices=estados, default=1, null=True, blank=True)
    class Meta:
        # db_table            = 'A01Aeg_Medico'
        verbose_name        = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering            = ["-created","user"]

    # class Meta:
    #     permissions = [
    #         ("Can_add_Paciente"   , "Puede crear paciente"),
    #         ("Can_view_Paciente"  , "Puede ver paciente"),
    #         ("Can_change_Paciente", "Puede modificar datos de un paciente")
    #         ]


    def __str__(self):
        return f'Dc. {self.user.last_name},{self.user.first_name}'

# *NIVELES DE LAS ALERGIAS
# Leve: Síntomas como estornudos, picazón en los ojos o piel, y congestión nasal. No suelen interferir gravemente con la vida diaria.
# Moderado: Síntomas más molestos, como urticaria, erupciones cutáneas, y problemas respiratorios leves. Pueden requerir medicación para controlar los síntomas.
# Severo (Anafilaxia): Reacción alérgica grave que puede causar dificultad para respirar, hinchazón de la garganta, y una caída brusca de la presión arterial. Esta condición es potencialmente mortal y requiere atención médica inmediata.

# *TIPOS DE ALERGIAS
# Alergias Respiratorias: causadas por alérgenos en el aire como el polvo, el polen, el moho, y los ácaros del polvo.
# Alergias a Medicamentos: reacciones adversas a medicamentos como penicilina, aspirina, y ciertos antibióticos.
# Alergias a Insectos: reacciones a picaduras de insectos como abejas, avispas, y mosquitos.
# Alergias a Animales: causadas por la caspa de mascotas como gatos y perros.
# Alergias de Contacto: reacciones a sustancias que tocan la piel, como el látex, níquel en joyería, o ciertos productos químicos.


class Paciente(models.Model):
    user        = models.OneToOneField(User, on_delete=models.RESTRICT,related_name='pacientes', verbose_name='Paciente',help_text='Usuario con perfil de paciente')
    image       = models.ImageField(default='/img_no_disp.png',upload_to="usuarios")
    dni         = models.CharField(max_length=10, null=True,blank=True)
    nacim       = models.DateField(blank=True, null=True)
    phone       = models.CharField(max_length=12,null=True, blank=True)
    generos     = (('M','Masculino'),('F','Femenino'),('O','Otro'))
    genero      = models.CharField(choices= generos, max_length=10,null=True, blank=True)
    salud       = models.ForeignKey(Isapre, on_delete=models.RESTRICT,null=True, blank=True)
    gruposSangre= (('1','0-'),('2','0+'),('3','A-'),('4','A+'),('5','B-'),('6','B+'),('7','AB-'),('8','AB+'),('9','Otro'))
    grupoSangre = models.CharField(choices= gruposSangre, max_length=4,null=True, blank=True)
    enfPrev     = models.TextField(max_length=200,null=True, blank=True)
    cirugPrev   = models.TextField(max_length=200,null=True, blank=True)
    contacto    = models.TextField(max_length=200,null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, null=True)
    estados     = (('0','Sin actividad'),('1','Con hora tomada'),('2','Exámenes pendientes'),('3','Diagnosticado'),('4','Eliminado'))
    estado      = models.CharField(max_length=20, default=0,choices=estados,null=True, blank=True)

    # * OTROS ATRIBUTOS DEL PACIENTE
    # * alergias, enf crónicas, medicamentos actuales, cirugías previas, contacto de emergencia

    class Meta:
        # db_table            = 'A01Seg_Paciente'
        verbose_name        = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering            = ["-created","user"]

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.nacim.year - ((hoy.month, hoy.day) < (self.nacim.month, self.nacim.day))
        return edad

    def cumple_hoy(self):
        hoy = date.today()
        if hoy.month == self.nacim.month and  hoy.day == self.nacim.day:
            cumple = True
            #TODO send email
        else:
            cumple = False
            return cumple

    def __str__(self):
        return f'Paciente {self.user.last_name},{self.user.first_name}'



class Funcionario(models.Model):
    user        = models.OneToOneField(User, on_delete=models.RESTRICT,related_name='funcionarios', verbose_name='Funcionario',help_text='Usuario con perfil de funcionario')
    image       = models.ImageField(default='/img_no_disp.png',upload_to="usuarios")
    dni         = models.CharField(max_length=10, null=True,blank=True)
    nacim       = models.DateField(blank=True, null=True)
    phone       = models.CharField(max_length=12,null=True, blank=True)
    cargo       = models.CharField(max_length=50, verbose_name="Cargo")
    created     = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table            = 'A01Aeg_Funcionario'
        verbose_name        = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering            = ["-created","user"]
    def __str__(self):
        return f'Colaborador {self.user.last_name},{self.user.first_name}'







# *Anterior modelo de usuario abc
# class Usuario(models.Model):
#     image       = models.ImageField(default='/img_no_disp.png',upload_to="usuarios")
#     direccion   = models.CharField(max_length=100,null=True, blank=True)
#     comuna      = models.CharField(max_length=50,null=True, blank=True)
#     pais        = models.CharField(max_length=20,null=True, blank=True)
#     generos     = (('M','Masculino'),('F','Femenino'),('O','Otro'))
#     genero      = models.CharField(choices= generos, max_length=10,null=True, blank=True)
#     estadosCiv  = (('S','Soltero'),('C','Casado'),('V','Viudo'),('P','Separado'))
#     estadoCiv   = models.CharField(choices= estadosCiv, max_length=10,null=True, blank=True)
#     nacim       = models.DateField(blank=True, null=True)
#     created     = models.DateTimeField(auto_now_add=True, null=True)
#     phone       = models.CharField(max_length=12,null=True, blank=True)
#     dni         = models.CharField(max_length=10, null=True,blank=True)
#     isActive    = models.BooleanField(verbose_name="Es activo", default=True)
#     class Meta:
#         abstract            = True





# def CreatePaciente(sender, instance, created,**kwargs): # *Crear el perfil de paciente
#     # print('sender ---------------> ',sender)
#     #        sender --------------->  <class 'django.contrib.auth.models.User'>
#     # print('instance -------------> ',instance)
#     #        instance ------------->  admin
#     # print('kwargs  --------------> ', **kwargs)
#     #         No imprimionada y se cayó
#     if created and instance.is_superuser == False:
#         Paciente.objects.create(user=instance)

# def save_user_profile(sender,instance,**kwargs): # *Graba datos en caso
#     instance.paciente.save()

# post_save.connect(CreatePaciente, sender=User) # *funcion que recibe señal y modelo que la envía

# post_save.connect(save_user_profile, sender=User)




# def CreateMedico(sender, instance, created,**kwargs): # *Crear el perfil de paciente
#     if created and instance.is_superuser == False:
#         Medico.objects.create(user=instance)

# def save_user_medprofile(sender,instance,**kwargs): # *Graba datos en caso
#     instance.medico.save()

# post_save.connect(CreateMedico, sender=User) # *funcion que recibe señal y modelo que la envía

# post_save.connect(save_user_medprofile, sender=User)