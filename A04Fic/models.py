from django.db import models
from django.contrib.auth.models import User
from A01Seg.models import *



# Create your models here.
class FichaPaciente(models.Model):
    fecha       = models.DateField( verbose_name="Fecha")
    paciente    = models.ForeignKey( Paciente, on_delete=models.RESTRICT, related_name="fichas")
    medico      = models.ForeignKey( Medico, on_delete=models.RESTRICT, related_name='medicos')
    sistole     = models.CharField( max_length=10, verbose_name="Presión Sistólica", blank=True, null=True)
    diastole    = models.CharField( max_length=10, verbose_name="Presión Diastólica", blank=True, null=True)
    altura      = models.CharField( max_length=10, verbose_name="Altura (cm)", blank=True, null=True)
    motivo      = models.TextField( max_length=500, verbose_name="Motivo de Consulta", blank=True, null=True)
    sintomas    = models.TextField( max_length=500, verbose_name="Sintomatología", blank=True, null=True)
    evaPre      = models.TextField(max_length=500,verbose_name="Evaluación Preliminar", blank=True, null=True)
    diagnosis   = models.TextField(max_length=500,verbose_name="Diagnósis", blank=True, null=True)
    posologia   = models.TextField(max_length=500,verbose_name="Tratamiento y Posología", blank=True, null=True)
    notas       = models.TextField(max_length=500,verbose_name="Notas del Médico", blank=True, null=True)
    hei_cm      = models.FloatField(default=0, blank= True, null= True)
    wei_gr      = models.FloatField(default=0, blank= True, null= True)
    sist        = models.FloatField(default=0, blank= True, null= True)
    diast       = models.FloatField(default=0, blank= True, null= True)
    temp        = models.FloatField(default=0, blank= True, null= True)

    class Meta:
        verbose_name        = 'Ficha De Paciente'
        verbose_name_plural = 'Fichas Del Paciente'
        ordering            = ['id']

    def max_hei(self, get_paciente):
        consulta = self.objects.filter(paciente=get_paciente).values('hei_cm').order_by('-hei_cm')[0]
        return consulta

    def __str__(self):
        return f'Ficha: {self.id} / Paciente: {self.paciente} / Fecha: {self.fecha}'

