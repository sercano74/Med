from dataclasses import fields
from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from .models import Paciente
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class FormPacienteCreate(ModelForm):
    class Meta:
        model = Paciente
        fields = ('image','genero','nacim','phone','grupoSangre','salud','estado')
        exclude = ('user',)

# class UserUpdateForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email']


# class PerfilUpdateForm(ModelForm):
#     class Meta:
#         model = Perfil
#         fields= ['nacim','direccion','numero','comuna','image']
#         exclude = ['user']

