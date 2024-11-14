from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import *
from A04Fic.models import *

from django.db.models import Sum,Avg,Min,Max
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404 as go404

from django.contrib import messages

# import matplotlib.pyplot as plt
# import pandas as pd

# Create your views here.
@login_required
def Fichas(request):
    objetos     = FichaPaciente.objects.all()


    permisos    = Permission.objects.filter(user=request.user)
    print('permisos #######################################     ',permisos)

    Qs = request.user.get_all_permissions()
    print('Qs ------------------------------------------>>>>>  ',Qs)

    que_perms = request.user.has_perms(Qs)
    print('que_perms &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  ',que_perms)

    puede_crear_ficha = request.user.has_perm('A04Fic.add_fichapaciente')
    print('puede_crear_ficha ----------->>>>>    ',puede_crear_ficha)


    return render(request,'A04Fic/Fichas.html',locals())


@login_required
def FichaCreate (request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        paciente_id    = request.GET.get('paciente', None)
        fichas = None
        if paciente_id:
            get_paciente = go404(Paciente, pk=paciente_id)
            fs_paciente  = FichaPaciente.objects.filter(paciente=get_paciente)
            n_fs_paciente  = FichaPaciente.objects.filter(paciente=get_paciente).count()

            sum_sist    = 0
            sum_diast   = 0
            sum_hei     = 0
            sum_wei     = 0
            for ficha in fs_paciente:
                sum_sist  += ficha.sist
                sum_diast += ficha.diast
                sum_hei   += ficha.hei_cm
                sum_wei   += ficha.wei_gr
            prom_sist   = round(sum_sist/n_fs_paciente,2)
            prom_diast  = round(sum_diast/n_fs_paciente,2)
            prom_hei    = round(sum_hei/n_fs_paciente,2)
            prom_wei    = round(sum_wei/n_fs_paciente,2)

            imc = round((prom_wei)/(prom_hei/100)**2,2)

            if sum_sist == 0:
                Q_max_hei = FichaPaciente.objects.filter(paciente=get_paciente).values('hei_cm').order_by('-hei_cm')[:1]
                last_5_wei = FichaPaciente.objects.filter(paciente=get_paciente).values('wei_gr').order_by('-wei_gr')[:5]
                last_2_temp = FichaPaciente.objects.filter(paciente=get_paciente).values('temp')[0:3]
                # Q_max_hei = FichaPaciente.objects.max_hei(get_paciente.id)
                # # max_hei=Q_max_hei[0]
                # paciente_prom_sist = Paciente.objects.annotate(prom_sist = Avg('fichas__sist'))
                # print('Prom Sistólica --------------------->     ',paciente_prom_sist[1].prom_sist)
                # prom_sist = paciente_prom_sist[1].prom_sist
                pass


        medicos = Medico.objects.all()
        return render(request, 'A04Fic/FichaCreate.html',locals())

    if request.method == 'POST':
        objeto          = FichaPaciente()
        objeto.fecha    = request.POST['fecha']
        paciente_id     = request.POST['paciente']
        paciente        = Paciente.objects.get(pk=paciente_id)
        objeto.paciente = paciente
        if request.user.username == 'admin':
            usert       = User.objects.get(username='medico2')
            medico      = Medico.objects.get(user=usert)
        else:
            medico      = Medico.objects.get(user=request.user)
        objeto.medico   = medico
        objeto.hei_cm   = request.POST['hei_cm']
        objeto.wei_gr   = request.POST['wei_gr']
        objeto.sist     = request.POST['sist']
        objeto.diast    = request.POST['diast']
        objeto.temp     = request.POST['temp']
        objeto.motivo   = request.POST['motivo']
        objeto.sintomas = request.POST['sintomas']
        objeto.evaPre   = request.POST['evaPre']
        objeto.diagnosis= request.POST['diagnosis']
        objeto.posologia= request.POST['posologia']
        objeto.notas    = request.POST['notas']
        objeto.save()

        messages.success(request," 👍 Médico added successfully! ")
        # return HttpResponseRedirect(reverse('A04Fic:FichaRead',args=[str(objeto.id)]))
        return render(request,'A04Fic/Fichas.html',locals())


@login_required
def FichaRead (request,pk):
    if request.method == 'GET':
        objeto = FichaPaciente.objects.get(id=pk)

        # edad = paciente.calcular_edad()
        # cumple =  paciente.cumple_hoy()

        if objeto.fecha:
            fn = objeto.fecha
            fn = str(fn.year)+"-"+str(fn.month)+"-"+str(fn.day)

        fs_paciente     = FichaPaciente.objects.filter(paciente=objeto.paciente).order_by('-fecha')
        n_fs_paciente   = FichaPaciente.objects.filter(paciente=objeto.paciente).count()

        sum_sist    = 0
        sum_diast   = 0
        sum_hei     = 0
        sum_wei     = 0
        for ficha in fs_paciente:
            sum_sist  += ficha.sist
            sum_diast += ficha.diast
            sum_hei   += ficha.hei_cm
            sum_wei   += ficha.wei_gr
        prom_sist   = round(sum_sist/n_fs_paciente,2)
        prom_diast  = round(sum_diast/n_fs_paciente,2)
        prom_hei    = round(sum_hei/n_fs_paciente,2)
        prom_wei    = round(sum_wei/n_fs_paciente,2)

        imc = round((prom_wei)/(prom_hei/100)**2,2)

        return render(request, 'A04Fic/FichaRead.html',locals())


@login_required
def FichaUpdate (request,pk):
    pass








#* Apuntes Médicos###################################################################################
#* El Índice de Masa Corporal (IMC) es una medida que se utiliza para determinar si una persona tiene un peso saludable en relación con su altura. Se calcula utilizando la siguiente fórmula:

# IMC = peso(kg) / altura(m)^2

# Donde:
# Peso se mide en kilogramos (kg).
# Altura se mide en metros (m).

# Ejemplo de cálculo: Si una persona pesa 70 kg y mide 1.75 m, su IMC se calcularía de la siguiente manera:

#* Interpretación del IMC:

# IMC inferior a 18.5: Bajo peso.
# IMC entre 18.5 y 24.9: Peso normal.
# IMC entre 25 y 29.9: Sobrepeso.
# IMC de 30 o más: Obesidad.

# El IMC es una herramienta útil para identificar posibles problemas de salud relacionados con el peso, aunque no considera factores como la composición corporal, el tipo de cuerpo o la distribución de grasa, por lo que debe utilizarse como una guía general y no como un diagnóstico definitivo.


#* ############################      PRESION ARTERIAL      ############################
# La presión arterial es una medida importante de la salud cardiovascular. Se expresa en dos números: la presión sistólica (el número superior) y la presión diastólica (el número inferior). La presión sistólica mide la presión en las arterias cuando el corazón late, mientras que la presión diastólica mide la presión en las arterias cuando el corazón está en reposo entre latidos.

# * Categorías de Presión Arterial

#? Presión Arterial Normal:
# Sistólica: Menos de 120 mm Hg
# Diastólica: Menos de 80 mm Hg

#? Presión Arterial Elevada:
# Sistólica: 120-129 mm Hg
# Diastólica: Menos de 80 mm Hg

#? Hipertensión Etapa 1:
# Sistólica: 130-139 mm Hg
# Diastólica: 80-89 mm Hg

#? Hipertensión Etapa 2:
# Sistólica: 140 mm Hg o más
# Diastólica: 90 mm Hg o más

#! Crisis Hipertensiva (Necesita atención médica inmediata):
# Sistólica: Más de 180 mm Hg
# Diastólica: Más de 120 mm Hg
