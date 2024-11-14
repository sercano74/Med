from django.shortcuts import render
from django.contrib.auth.models import User

from .models import *
from .forms import UserRegisterForm, FormPacienteCreate

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404 as go404

from django.contrib import messages

# Create your views here.

# Ingresar ya estando logeado
def signin(request):
    if request.method == 'GET':
        return render(request, 'A01Seg/signin.html', { 'form':AuthenticationForm})
    else:
        user = authenticate (request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # request.session['usernameit'] = user.username
            return render(request, 'A01Seg/signin.html', { 'form':AuthenticationForm, 'error':'Username or password is incorrect'})

        else:
            login (request, user)
            return redirect ('home')



# Salir o deslogearse
def signout(request):
    logout(request)
    return redirect('home')
#https://www.youtube.com/watch?v=Z3x-4G6oVlQ



# * Crear usuario
# def signup(request):
#     if request.method == 'GET':
#         # print('GET: Dispone formulario signup')
#         return render(request, 'A01Seg/signup.html', {'form': UserRegisterForm})
#     else:
#         # print('POST: Capturando lo registrado en formulario signup')
#         # print(request.POST['first_name'] , request.POST['password2'], request.POST)
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     first_name = request.POST['first_name'],
#                     last_name  = request.POST['last_name'],
#                     username   = request.POST['username'],
#                     email      = request.POST['email'],
#                     password   = request.POST['password1']
#                 )
#                 user.save()

#                 rol = request.POST['rol']
#                 if rol=='Pac':
#                     paciente = Paciente.objects.create(user=user,estado=0)
#                     # paciente.save()
#                     # CreatePaciente()
#                     # CreatePaciente.save()
#                     # request.session['paciente']=CreatePaciente
#                     login(request, user)
#                     return render(request, 'A01Seg/PacienteUpdate.html')

#                 login(request, user)
#                 return redirect('home')

#             except:
#                 return render(request, 'A01Seg/signup.html', {'form': UserRegisterForm, 'Error': 'Maybe could yet exists'})

#         return render(request, 'A01Seg/signup.html', {'form': UserRegisterForm, 'Error': 'Password do not match'})



# * Crear usuario
def UsuarioCreate(request):
    if request.method == 'GET':
        return render(request, 'A01Seg/UsuarioCreate.html')

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                new_user = User.objects.create_user(
                    first_name = request.POST['first_name'],
                    last_name  = request.POST['last_name'],
                    username   = request.POST['username'],
                    email      = request.POST['email'],
                    password   = request.POST['password1']
                )
                new_user.save()

                request.session['new_user_id'] = new_user.id

                rol = request.POST['rol']

                if rol=='Pac':
                    return HttpResponseRedirect(reverse('A01Seg:PacienteCreate'))

                if rol == 'Med':
                    return HttpResponseRedirect(reverse('A01Seg:MedicoCreate'))

                else:
                    return redirect('home')

            except:
                return render(request, 'A01Seg/signup.html', {'form': UserRegisterForm, 'Error': 'Maybe could yet exists'})

        return render(request, 'A01Seg/signup.html', {'form': UserRegisterForm, 'Error': 'Password do not match'})

def Pacientes(request):
    pacientes  = Paciente.objects.exclude(estado='4')
    now = date.today()
    return render(request,'A01Seg/Pacientes.html',locals())

def PacienteCreate(request):
    if request.method == 'GET':
        new_user_id = int(request.session.get('new_user_id'))
        new_user = User.objects.get(pk=new_user_id)
        isapres = Isapre.objects.all()
        return render(request, 'A01Seg/PacienteCreate.html',locals())

    if request.method == 'POST':
        # largo=Paciente.objects.all().count()+1
        # print('largo ----------------->   ',largo)
        new_user_id = int(request.session.get('new_user_id'))
        new_user    = User.objects.get(pk=new_user_id)

        new = Paciente()
        new.user    = new_user
        new.image   = request.FILES.get('image')
        new.dni     = request.POST['dni']
        new.save()

        messages.success(request," 👍 Paciente added successfully! ")
        return HttpResponseRedirect(reverse('A01Seg:PacienteRead',args=[str(new.id)]))

def PacienteRead(request,pk):
    if request.method == 'GET':
        paciente = Paciente.objects.get(id=pk)
        edad = paciente.calcular_edad()
        cumple =  paciente.cumple_hoy()
        print('Cumple 😘🌻🍀 ', cumple)
        if paciente.nacim:
            fn = paciente.nacim
            fn = str(fn.year)+"-"+str(fn.month)+"-"+str(fn.day)
        return render(request, 'A01Seg/PacienteRead.html',locals())

def PacienteUpdate(request,pk):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(id=pk)
            if paciente.nacim:
                fn = paciente.nacim
                fn = str(fn.year)+"-"+str(fn.month)+"-"+str(fn.day)
            isapres = Isapre.objects.all()
            return render(request, 'A01Seg/PacienteUpdate.html',locals())
        except:
            message="Paciente seleccionado, no existe o está inactivo !!"
            return render(request, '404.html', locals())
    if request.method == 'POST':
        # try:
        isapres     = Isapre.objects.all()
        paciente    = go404(Paciente,id=pk)
        usert        = User.objects.get(username= paciente.user.username)

        if request.FILES.get('image') != None and paciente.image == None:
            paciente.image  = request.FILES.get('image')
        else:
            paciente.image = paciente.image
        if request.POST['dni']:
            paciente.dni    = request.POST['dni']
        if request.POST['nacim']:
            nacim = request.POST['nacim']
            paciente.nacim  = request.POST['nacim']
        if request.POST['phone']:
            paciente.phone  = request.POST['phone']
        if request.POST['genero']:
            paciente.genero = request.POST['genero']
        if request.POST['grupoSangre']:
            paciente.grupoSangre = request.POST['grupoSangre']
        if request.POST['salud']:
            isapre_id =request.POST['salud']
            isapre = Isapre.objects.get(pk=isapre_id)
            paciente.salud  = isapre
        paciente.save()

        if request.POST['first_name']:
            first_name = request.POST['first_name']
            usert.first_name = first_name
        if request.POST['last_name']:
            usert.last_name = request.POST['last_name']
        if request.POST['email']:
            usert.email    = request.POST['email']
        usert.save()

        paciente = go404(Paciente,id=pk)
        messages.success(request," 👍 Paciente modified successfully! ")
        return HttpResponseRedirect(reverse('A01Seg:PacienteRead',args=[str(paciente.id)]))
        # except:
        #     message="Paciente seleccionado, no existe o está inactivo !!"
        #     return render(request, '404.html', locals())

def PacienteDelete(request,pk):
    paciente = Paciente.objects.get(id=pk)
    paciente.estado = '4'
    paciente.save()
    messages.success(request," 👍 Paciente deleted softly, successfully! ")
    pacientes = Paciente.objects.exclude(estado = '4')
    return render(request, 'A01Seg/Pacientes.html',locals())



# *###################### GESTIÓN DE LOS MÉDICOS ###########################
def Medicos(request):
    medicos = Medico.objects.exclude(estado = 0)
    return render(request,'A01Seg/Medicos.html',locals())

# *Crear Médico (sólo datos del usu)
def MedicoCreate(request):
    if request.method == 'GET':
        new_user_id = int(request.session.get('new_user_id'))
        new_user = User.objects.get(pk=new_user_id)
        return render(request, 'A01Seg/MedicoCreate.html',locals())

    if request.method == 'POST':
        new_user_id = int(request.session.get('new_user_id'))
        new_user    = User.objects.get(pk=new_user_id)
        if new_user:
            return redirect ('home')
        else:
            new = Medico()
            new.user    = new_user
            new.image   = request.FILES.get('image')
            new.dni     = request.POST['dni']
            new.save()
            request.session['new_user_id'] == None #*Borramos la variable de apoyo

            messages.success(request," 👍 Médico added successfully! ")
            return HttpResponseRedirect(reverse('A01Seg:MedicoRead',args=[str(new.id)]))

def MedicoRead(request,pk):
    if request.method == 'GET':
        objeto = Medico.objects.get(id=pk)
        if objeto.nacim:
            fn = objeto.nacim
            fn = str(fn.year)+"-"+str(fn.month)+"-"+str(fn.day)
        return render(request, 'A01Seg/MedicoRead.html',locals())

def MedicoUpdate(request,pk):
    if request.method == 'GET':
        try:
            objeto = Medico.objects.get(id=pk)
            if objeto.nacim:
                fn = objeto.nacim
                fn = str(fn.year)+"-"+str(fn.month)+"-"+str(fn.day)
            return render(request, 'A01Seg/MedicoUpdate.html',locals())

        except:
            message="Medico seleccionado, no existe o está inactivo !!"
            return render(request, '404.html', locals())

    if request.method == 'POST':
        try:
            objeto = go404(Medico,id=pk)
            if request.POST['dni']:
                objeto.dni    = request.POST['dni']
            if request.FILES.get('image') != None and objeto.image == None:
                objeto.image  = request.FILES.get('image')
            else:
                objeto.image = objeto.image
            if request.POST['nacim']:
                objeto.nacim  = request.POST['nacim']
            if request.POST['phone']:
                objeto.phone  = request.POST['phone']
            if request.POST['especialidad']:
                objeto.especialidad  = request.POST['especialidad']
            if request.POST['experiencia']:
                objeto.experiencia  = request.POST['experiencia']

            objeto.save()

            objeto = go404(Medico,id=pk)

            messages.success(request," 👍 Medico modified successfully! ")
            return HttpResponseRedirect(reverse('A01Seg:MedicoRead',args=[str(objeto.id)]))
        except:
            message="Medico seleccionado, no existe o está inactivo !!"
            return render(request, '404.html', locals())

def MedicoDelete(request,pk):
    medico = Medico.objects.get(id=pk)
    medico.estado = 0
    medico.save()
    medicos = Medico.objects.exclude(estado = 0)
    messages.success(request," 👍 Medico deleted successfully! ")
    return render(request, 'A01Seg/Medicos.html',locals())