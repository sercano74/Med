from django.urls import path
from .views import *

app_name = 'A01Seg'

urlpatterns = [
    # path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('signout/', signout, name="signout"),

    path('UsuarioCreate/', UsuarioCreate, name='UsuarioCreate'),

    path('Pacientes/',Pacientes, name='Pacientes'),
    path('PacienteCreate/',PacienteCreate,name="PacienteCreate"),
    path('PacienteRead/<int:pk>',PacienteRead,name="PacienteRead"),
    path('PacienteUpdate/<int:pk>',PacienteUpdate,name="PacienteUpdate"),
    path('PacienteDelete/<int:pk>',PacienteDelete,name="PacienteDelete"),

    path('Medicos/',Medicos, name='Medicos'),
    path('MedicoCreate/',MedicoCreate,name="MedicoCreate"),
    path('MedicoRead/<int:pk>',MedicoRead,name="MedicoRead"),
    path('MedicoUpdate/<int:pk>',MedicoUpdate,name="MedicoUpdate"),
    path('MedicoDelete/<int:pk>',MedicoDelete,name="MedicoDelete"),

    # path('contactar/', contactar, name="contactar"),
    # path('perfilView/', perfilView, name="perfilView"),
    # path('perfilEdit/', perfilEdit, name="perfilEdit"),

]

